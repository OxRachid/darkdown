#!/usr/bin/env python3
import subprocess

from . import colors as c
from . import functions as fun
from . import headerscreen as header


def get_resolutions():
    # List of resolutions
    resolutions = [
        "2160",
        "1440",
        "1080",
        "720",
        "480",
        "360",
        "240",
    ]
    return resolutions


# Function to handle the download using yt-dlp
def download_video(user_choice, video_url, resolutions):
    resolution = resolutions[user_choice]
    print(c.color_text(f" ➡ Downloading video in {resolution}p...", c.BRIGHT_YELLOW))

    # Command to run yt-dlp with format selection
    command = [
        "yt-dlp",
        "-f",
        f"bestvideo[height<={resolution}][tbr<=20000]+bestaudio",
        "-S",
        "ext:mp4:m4a,proto:https:m3u8,vcodec:avc1:av01:vp09,res,br,tbr",
        "-o",
        fun.video_output_path,
        video_url,
        "--quiet",  # Quiet mode
        "--progress",  # Show progress
    ]

    # Run the command using subprocess
    result = subprocess.run(command)
    # Check if there was an error
    if result.returncode != 0:
        fun.handle_error(result.stderr)  # Print the error message
    else:
        print(c.color_text(" Video downloaded ✓", c.GREEN, c.BOLD))
        print(c.color_text(f" Video path : [{fun.config["Paths"]["video_dir"]}]", c.BRIGHT_GREEN, c.BOLD))


# Function to download audio (optional)
def download_audio(url):
    command = [
        "yt-dlp",
        "-f",
        "bestaudio",
        "-o",
        fun.audio_output_path,  # Output path for audio
        "--quiet",  # Quiet mode
        "--progress",  # Show progress
        url,
    ]
    print(c.color_text(" ➡ Downloading the best audio...", c.BRIGHT_YELLOW))
    # Run the command using subprocess
    result = subprocess.run(command)
    # Check if there was an error
    if result.returncode != 0:
        fun.handle_error(result.stderr)  # Print the error message
    else:
        print(c.color_text(" Audio downloaded ✓", c.GREEN, c.BOLD))
        print(c.color_text(f" Audio path : [{fun.config["Paths"]["audio_dir"]}]", c.BRIGHT_GREEN, c.BOLD))


def perform_downloading(resolutions, video_url):
    user_choice = fun.get_user_option(0, len(resolutions) + 1, "\n[*] Select Your Format: ")

    fun.exit_option(user_choice, len(resolutions) + 1)

    if user_choice == 0:
        download_audio(video_url)
    else:
        download_video(user_choice - 1, video_url, resolutions)


def main():
    # display header screen
    header.display_header()

    fun.title_screen("    * Normal download *")

    # Get the user input on a new line
    video_url = fun.get_video_url()

    # List of resolutions
    resolutions = get_resolutions()

    # display resolutions
    fun.print_resolutions(resolutions)

    # Warning
    fun.select_warning()

    # perform_downloading
    perform_downloading(resolutions, video_url)


if __name__ == "__main__":
    main()
