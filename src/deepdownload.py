#!/usr/bin/env python3
import json
import subprocess
from time import sleep

from . import colors as c
from . import functions as fun
from . import headerscreen as header


# Get bitrate of format
def get_bitrate(format_info):
    # Get the total bitrate, whether it's audio, video, or combined
    bitrate = format_info.get("tbr") or format_info.get("vbr") or format_info.get("abr")
    return (bitrate) if bitrate else None


# find max or min bitrate in specific cases
def find_max_bitrate(available_formats):
    # Step 1: Check for the max bitrate for SDR formats
    sdr_formats = [
        f for f in available_formats if f.get("ext") == "mp4" and f.get("protocol") in ["https", "http"] and f.get("dynamic_range") == "SDR"
    ]

    # If SDR formats exist, return the one with the highest bitrate
    if sdr_formats:
        max_sdr_format = max(sdr_formats, key=lambda f: f.get("tbr", 0))
        return max_sdr_format.get("tbr", max_sdr_format.get("vbr", 0))

    # Step 2: If no SDR formats, check for HDR formats
    hdr_formats = [
        f
        for f in available_formats
        if f.get("ext") == "mp4" and f.get("protocol") == "https" and f.get("dynamic_range") in ["HDR", "HDR10", "HDR10+", "HDR12"]
    ]

    # If HDR formats exist, return the one with the lowest bitrate
    if hdr_formats:
        min_hdr_format = min(hdr_formats, key=lambda f: f.get("tbr", 0))
        return min_hdr_format.get("tbr", min_hdr_format.get("vbr", 0))

    # If neither SDR nor HDR formats are found, return None
    return None


# Give and get format properties
def get_format_priority(format_info):
    ext = format_info["ext"]
    protocol = format_info["protocol"]
    hdr = format_info.get("dynamic_range", None)
    # Create a tuple of boolean values
    return (
        ext == "mp4",
        protocol == "https",
        hdr == "SDR",
        protocol == "m3u8",
        ext == "webm",
    )


def sort_key(format_info):
    # Combine priority tuple with resolution and bitrate
    return (
        get_format_priority(format_info),
        format_info.get("height"),  # Make sure to use 'height'
        format_info.get("tbr"),  # Make sure to use 'bitrate'
    )


# Get Formats id
def get_formats_id(formats_info, highest_bitrate, chosen_resolution):
    print(c.color_text("\n┌────────────────────────────────────────────────────┐", c.YELLOW))
    print(c.color_text(f"            * Available Formats [{chosen_resolution}p] * ", c.BRIGHT_RED, c.BOLD))
    print(c.color_text("└────────────────────────────────────────────────────┘", c.YELLOW))
    format_IDs = {}
    for i, formatInfo in enumerate(formats_info, 1):
        size = formatInfo.get("filesize") or formatInfo.get("filesize_approx") or formatInfo.get("size")
        proto = formatInfo.get("protocol", "N/A")
        format_proto = "m3u8_n" if proto == "m3u8_native" else proto
        formated_size = fun.format_size(size)
        # Check if highest_bitrate is not None before making the comparison
        recommended = (
            c.color_text("[R]", c.BRIGHT_GREEN, c.BOLD) if highest_bitrate is not None and highest_bitrate == get_bitrate(formatInfo) else "   "
        )
        index_str = f"[{i}]"  # Convert index to string with brackets
        sleep(0.1)
        print(
            c.color_text(
                f"│ {index_str:<6} {formatInfo.get('ext', 'N/A'):<6} "
                f" {format_proto:<8} "
                f" {formatInfo.get('dynamic_range', 'N/A'):<6} "
                f" {formated_size:<11} {recommended}"
                f"   │".strip(),
                c.BRIGHT_YELLOW,
            )
        )

        format_IDs[i] = formatInfo.get("format_id", "N/A")  # Store the format code
    index_str = f"[{len(formats_info)+1}]"
    print(c.color_text(f"│ {index_str:<6} Exit                                        │", c.BRIGHT_RED))
    print(c.color_text("└────────────────────────────────────────────────────┘", c.YELLOW))
    print(c.color_text("*[R] = Recommended", c.BRIGHT_GREEN))
    return format_IDs


# Add unique height to the set
def get_unique_res(formats):
    unique_resolutions = set()
    for format in formats:
        height = format.get("height")
        ext = format.get("ext")
        if ext != "mhtml" and height and height > 144:
            unique_resolutions.add(height)

    return unique_resolutions


# func to fetch_formats as list of dectionaries
def fetch_formats(video_url):
    try:
        result = subprocess.run(
            ["yt-dlp", "-J", video_url],
            capture_output=True,
            text=True,
            check=True,
        )
        video_info = json.loads(result.stdout)
        return video_info["formats"]
    except subprocess.CalledProcessError as e:
        fun.handle_error(f"Unable to fetch formats: {e.stderr}")
    except json.JSONDecodeError:
        fun.handle_error("Failed to parse video information")


# Perform audio downloading
def download_audio(video_url):
    # Download the best audio
    print(c.color_text(" ➡ Downloading the best audio...", c.BRIGHT_YELLOW))
    fun.download_format("bestaudio/best", fun.audio_output_path, video_url)
    print("Audio downloaded ✓")
    print(c.color_text(" Audio downloaded ✓", c.GREEN, c.BOLD))
    print(c.color_text(f" Audio path : [{fun.config["Paths"]["audio_dir"]}]", c.BRIGHT_GREEN, c.BOLD))


# Perform video downloading
def download_video(formats, sorted_res_formats, format_choice, video_url):
    # display header screen
    header.display_header()

    fun.title_screen("    * Deep download *")

    # Extract the chosen resolution into a variable
    chosen_resolution = sorted_res_formats[format_choice - 1]

    # Extract all available resolutions of chosen_resolution
    available_res_formats = [f for f in formats if f.get("height") == chosen_resolution]

    # check where no valid formats are found after filtering
    fun.is_valid(available_res_formats)

    # Sort formats using the new method
    sorted_available_formats = sorted(available_res_formats, key=sort_key, reverse=True)

    # get highest_bitrate
    highest_bitrate = find_max_bitrate(sorted_available_formats)

    # Display sorted formats and get formats_id
    formats_IDs = get_formats_id(sorted_available_formats, highest_bitrate, chosen_resolution)

    # Step 8: Ask the user to select a specific format
    user_choice = fun.get_user_option(1, len(formats_IDs) + 1, "\n[*] select a format: ")

    fun.exit_option(user_choice, len(formats_IDs) + 1)

    chosen_format_code = formats_IDs[int(user_choice)]

    #  downloading the video with the specific format code
    print(c.color_text(" ➡ Downloading video...", c.BRIGHT_YELLOW))
    fun.download_format(chosen_format_code, fun.video_output_path, video_url)
    print(c.color_text(" Video downloaded ✓", c.GREEN, c.BOLD))
    print(c.color_text(f" Video path : [{fun.config["Paths"]["video_dir"]}]", c.BRIGHT_GREEN, c.BOLD))


def main():
    # display header screen
    header.display_header()

    fun.title_screen("    * Deep download *")

    # Ask user to enter video url
    video_url = fun.get_video_url()

    # Fetch formats
    formats = fetch_formats(video_url)

    # check formats Validate
    fun.is_valid(formats)

    # Initialize an empty set to store unique heights
    unique_resolutions = set()
    unique_resolutions = get_unique_res(formats)

    # Convert the set to a list and sort heights
    sorted_res_formats = sorted(unique_resolutions, reverse=True)

    # Display resolutions
    fun.print_resolutions(sorted_res_formats)

    # Display available format options and get user format choice
    format_choice = fun.get_user_option(0, len(sorted_res_formats) + 1, "\n[*] Enter Your Choice: ")

    fun.exit_option(format_choice, len(sorted_res_formats) + 1)

    # Step 6: Handle user choice
    if format_choice == 0:
        download_audio(video_url)
    else:
        download_video(formats, sorted_res_formats, format_choice, video_url)


if __name__ == "__main__":
    main()
