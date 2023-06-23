# Python Environment Setup Script

This is a bash script to ensure `python3` and `pip3` are installed on your system and setup a new Python virtual environment with popular Python packages.

## Requirements

- Bash shell
- Python3
- pip3

If Python3 and pip3 are not installed in your system, the script will remind you to install them first.

## Usage

1. Download the bash script to your local machine.
2. Change the permissions of the script file to make it executable:

    ```
    chmod +x pyguy.sh
    ```

3. Run the bash script in your terminal:

    ```
    ./pyguy.sh
    ```

The script will:

- Check if Python3 and pip3 are installed in your system.
- Create a virtual environment (this step is optional and can be removed or commented out if not needed).
- Upgrade pip3 to the latest version.
- Install popular Python3 packages which include `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `requests`, `beautifulsoup4`, `Flask`, `Django`, `sqlalchemy`, `pytest`, `jupyter`, `pylint`, `tensorflow`, `keras`, and `torch`.

At the end of the script, a message "All packages have been installed. Enjoy coding!" will appear to confirm the successful installation.

**Note:** The script creates a new Python virtual environment, so the installed packages will not affect your global Python environment. If you don't want to use the virtual environment, you can remove or comment out the relevant lines in the script.

## Troubleshooting

In case of any issues with the script execution:

- Ensure your terminal is running a Bash shell. Use `echo $SHELL` to check your current shell.
- Check if Python3 and pip3 are installed and in your PATH. You can verify this by running `python3 --version` and `pip3 --version`.
- Make sure you have the necessary permissions to install packages and create a virtual environment in the directory where you are running the script.
- Make sure you have an active internet connection, as the script needs to download packages from the internet.
