![Diagram](screenshot.jpg)

# Darkdown

A powerful YouTube video and audio downloader using yt-dlp

Features:
- Download YouTube videos in high quality from source servers
- Download audio in best quality
- Download video in a specific format (mp4/webm...etc)


## Requirements
- Python 3.6 or higher

## Installation and Usage Guide
To install Darkdown, follow these steps. 

in fact there are many ways of installation and you can choose any of them based on your main need...

# Quick installation
this is the easy way to install darkdown by just one command-line

copy and run it in your terminal

```bash
pip install git+https://github.com/OxRachid/darkdown.git
```

That's it! Now you can use Darkdown from anywhere:
```bash
darkdown
```
if you want to remove it run:
```bash
pip uninstall darkdown
```

## Alternative Installation (If you want to see the code)

1. Clone the repository:
```bash
git clone https://github.com/OxRachid/darkdown.git
cd darkdown
```

2. Run the installer:
```bash
pip install -e .
```

And now you can use darkdown by just type:
```bash
darkdown
```
to remove it:
```bash
pip uninstall darkdown
rm -rf ~/darkdown
```

## Release installation
1. Download the latest release from [darkdown releases](https://github.com/OxRachid/darkdown/releases) 
2. Extract the downloaded .zip or .tar.gz file.
3. In the extracted folder, run:
```bash
pip install -e .
```
4. Once installed, you can use darkdown as a command in the terminal

and you can remove it as the prv way

## Troubleshooting

If you encounter any issues:

1. Make sure Python is installed:
```bash
python --version
```

2. Try reinstalling:
```bash
pip uninstall darkdown
pip install git+https://github.com/OxRachid/darkdown.git
```

## Updates

To update to the latest version:
```bash
pip install --upgrade git+https://github.com/OxRachid/darkdown.git
```

## Recommendation(optional)
For best results, install within a virtual environment to avoid conflicts with other Python packages.

Here’s a sample steps and instractions for creating a virtual environment to install darkdown:
   
⦁ step 1: Create and Manage Global Virtual Environments 
   1. Create a centralized directory (Global directory for all virtual environments):
```bash
mkdir ~/venvs
```
   2. Create a unique virtual environment for darkdown progect in this directory:
```bash
python -m venv ~/venvs/darkdown_env
```  
   3. Activate the virtual environment:

     **On macOS/Linux**:
```bash
source ~/venvs/darkdown_env/bin/activate 
```
     **On Windows**:
```bash
~/venvs/darkdown_env\Scripts\activate 
```
⦁ Step 2: After activating the environment, you can now install darkdown using any of the above methods.

within this environment you’re free to run, develop, or test within darkdown without affecting your other python projects in your system. 

Then, you can deactivate the environment once you’re finished:
```bash
deactivate
```

### Default Storage Paths

Darkdown saves videos and audio files to default directories based on your operating system. You can modify these paths in the `config.ini` file.

| **Operating System** | **Default Video Path**                        | **Default Audio Path**                       |
|----------------------|-----------------------------------------------|----------------------------------------------|
| **Linux/macOS**      | `~/Videos/darkdown`                           | `~/Music/darkdown`                           |
| **Windows**          | `C:\Users\<YourName>\Videos\darkdown`         | `C:\Users\<YourName>\Music\darkdown`         |
| **Termux**           | `~/storage/shared/darkdown/videos`            | `~/storage/shared/darkdown/audios`           |

**Note**: If you are using Termux, you must first run `termux-setup-storage` to allow Darkdown access to shared storage. After granting permissions, Darkdown will save files to `~/storage/shared/darkdown`.

### Configuration

You can customize the storage paths by editing `config.ini` in the `Paths` section. For example:

```ini
[Paths]
video_dir = /path/to/your/video/directory
audio_dir = /path/to/your/audio/directory
