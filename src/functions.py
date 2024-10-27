#!/usr/bin/env python3
import configparser
import os
import re
import sys

import yt_dlp

import colors as c

# Load configuration
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config.ini")
config.read(config_path)

# Set paths for video and audio directories
VIDEODIR_PATH = os.path.expanduser(config["Paths"]["video_dir"])
AUDIODIR_PATH = os.path.expanduser(config["Paths"]["audio_dir"])

# Create the directories if they do not exist
os.makedirs(VIDEODIR_PATH, exist_ok=True)
os.makedirs(AUDIODIR_PATH, exist_ok=True)

# When downloading files, use the correct path with the filename pattern
video_output_path = os.path.join(VIDEODIR_PATH, "%(title)s_%(height)sp_%(format_id)s.%(ext)s")
audio_output_path = os.path.join(AUDIODIR_PATH, "%(title)s_%(height)sp_%(format_id)s.%(ext)s")


def handle_error(message):
    # Function to handle errors
    print(c.color_text(f"✖ Error: {message}", c.BRIGHT_RED))
    sys.exit(1)


# exit option for user
def exit_option(user_choice, length):
    if user_choice == length:
        print(c.color_text("Exiting...", c.MEDIUM_RED))
        sys.exit(0)


def is_valid(obj):
    if not obj:
        handle_error("No data found...")


def format_size(size_in_bytes):
    # Convert size from bytes to a more readable format (KB/MB/GB)
    if size_in_bytes is None:
        return "N/A"

    if size_in_bytes >= 1_073_741_824:  # GB
        return f"{size_in_bytes / 1_073_741_824:.2f} GB"
    elif size_in_bytes >= 1_048_576:  # MB
        return f"{size_in_bytes / 1_048_576:.2f} MB"
    elif size_in_bytes >= 1_024:  # KB
        return f"{size_in_bytes / 1_024:.2f} KB"
    else:
        return f"{size_in_bytes} Bytes"


# Validate the user choice
def get_user_option(start, end, prompt):
    while True:
        try:
            choice = int(input(c.color_text(prompt, c.BLUE, c.BOLD)))
            if start <= choice <= end:
                return choice
            print(c.color_text(" ✖ Invalid choice. Please try again.", c.BRIGHT_RED))
        except ValueError:
            print(c.color_text(" ✖ Please enter a number.", c.BRIGHT_RED))


# Display available resolutions
def print_resolutions(resolutions):
    print(c.color_text("┌───────────────┐", c.YELLOW))
    print(c.color_text(" * Resolutions * ", c.BRIGHT_RED, c.BOLD))
    print(c.color_text("└───────────────┘", c.YELLOW))
    print(c.color_text("│ [0] Audio     │", c.CYAN))
    for i, option in enumerate(resolutions, 1):
        padded_option = f"{option}p".ljust(10)
        print(c.color_text(f"│ [{i}] {padded_option}│", c.YELLOW))
    print(c.color_text(f"│ [{len(resolutions)+1}] Exit" + " " * 6 + "│", c.BRIGHT_RED))
    print(c.color_text("└───────────────┘", c.YELLOW))


def select_warning():
    print(c.color_text("┌────────────────────────────────────────┐", c.MEDIUM_RED))
    print(c.color_text("│ ❗Warning : Please select a resolution │ \n│  that your video is supported          │", c.MEDIUM_RED))
    print(c.color_text("└────────────────────────────────────────┘", c.MEDIUM_RED))


# check url Validate
def is_valid_youtube_url(url):
    patterns = [config["URL_Patterns"][key] for key in config["URL_Patterns"]]
    return any(re.match(pattern, url) for pattern in patterns)


def get_video_url():
    # Print the prompt message
    print(c.color_text("\n\n[*] Enter the video URL:", c.BLUE, c.BOLD))
    # Get the user input on a new line
    video_url = input().strip()
    if not is_valid_youtube_url(video_url):
        handle_error("Invalid URL. Please enter a valid YouTube URL.")

    return video_url


def download_format(format_code, output_path, video_url):
    ydl_opts = {
        "format": format_code,
        "outtmpl": output_path,
        "noplaylist": True,
        "quiet": True,  # Set to True to enable quiet mode
        "progress": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except yt_dlp.utils.DownloadError as e:
        handle_error(f"Network error or invalid URL: {str(e)}")
    except yt_dlp.utils.ExtractorError as e:
        handle_error(f"Extraction error: {str(e)}")
    except yt_dlp.utils.PostProcessingError as e:
        handle_error(f"Post-processing error: {str(e)}")
    except Exception as e:
        handle_error(f"An unexpected error occurred: {str(e)}")


def title_screen(promt):
    print(" " * 14 + c.color_text("╔════════════════════════════════╗   ", c.MEDIUM_RED))
    print(" " * 17 + c.color_text(promt, c.LIGHT_RED))
    print(" " * 14 + c.color_text("╚════════════════════════════════╝   ", c.MEDIUM_RED))
