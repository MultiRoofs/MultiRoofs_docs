# Installing dependencies

(installing-roofer)=
## Installing Roofer

**Roofer** performs fully automatic LoD2.2 building reconstruction from a classified point cloud
and building footprint (or roofprint) polygons. It was developed, and is still used, to create the
[3DBAG dataset](https://3dbag.nl/).

The easiest way to install Roofer is to download a ready-to-use release from GitHub, as described
below. Alternatively, you can use the [Docker image](https://hub.docker.com/r/3dgi/roofer/tags) or
[build Roofer from source](https://innovation.3dbag.nl/roofer/developers.html).

### Windows

1. Go to the [Roofer releases page](https://github.com/3DBAG/roofer/releases/latest) and download
   the file `roofer-windows-x86_64-v<version>.zip`, where `<version>` is the release number
   (1.0.0 or later).
2. Unzip the file in a folder of your choice, for example:

   `C:\Users\<you>\AppData\Local\Programs\roofer`

   The program `roofer.exe` is in the `bin` subfolder.
3. If your organisation allows it, add the `bin` folder to your user `PATH`, so that you can run Roofer 
from any folder. This does not require administrator rights, but some managed computers block it.
   1. Open the Start menu, search for **Edit environment variables for your account**, and open it.
   2. Under **User variables**, select **Path** and click **Edit**.
   3. Click **New** and paste the path to the `bin` folder, for example
      `C:\Users\<you>\AppData\Local\Programs\roofer\bin`.
   4. Click **OK** to close all windows.
   
```{note}
If you cannot change the `PATH`, you can still use Roofer by typing the full path to
`roofer.exe` instead of `roofer`, for example:

`C:\Users\<you>\AppData\Local\Programs\roofer\bin\roofer.exe --version`

Use the same full path in the commands of the tutorial.
```

4. Open a **new** Command Prompt and check the installation:

```
   roofer --version
```

```{note}
If Roofer is not on your `PATH`, replace roofer with the full path to `roofer.exe`.
```
   If the version number is shown, Roofer is ready to use.

```{figure} ../images/roofer_path.png
:alt: Windows dialog for editing the user Path variable with the Roofer bin folder added
:width: 80%
:align: center
:name: fig-roofer-path

Adding the Roofer `bin` folder to the user `PATH`.
```

### Linux and macOS

1. Go to the [Roofer releases page](https://github.com/3DBAG/roofer/releases/latest) and download
   the file `roofer-linux-x86_64-v<version>.zip`, where `<version>` is the release number
   (1.0.0 or later).
2. Unzip the file in a folder of your choice, for example:

   `/home/<you>/Downloads/`

   The program `roofer` is in the `bin` subfolder.

If the folder `~/.local/bin` is not yet on your `PATH`, add this line to your shell profile
(for example `~/.bashrc` or `~/.zshrc`) and open a new terminal:

```
export PATH="$HOME/.local/bin:$PATH"
```

3. Give execute permissions to the `roofer` file:

```
chmod +x /home/<you>/Downloads/roofer-linux-x86_64-v1.0.0/bin/roofer
```

Then check the installation:

```
roofer --version
```

For more details, see the [Roofer installation guide](https://innovation.3dbag.nl/roofer/getting_started.html).

## Installing cjseq

[cjseq](https://github.com/cityjson/cjseq) is an open-source tool for converting between CityJSONSeq and CityJSON.

1. Install the Rust toolchain by following the instructions at
   [rust-lang.org](https://www.rust-lang.org/learn/get-started).

   Installing Rustup also installs the latest stable versions of the Rust compiler and its package manager, `cargo`.

```{note}
   On Linux and macOS, `cargo` is installed in `~/.cargo/bin`, which is only added to your PATH in new terminal sessions. If `cargo` is not found after installing, open a new terminal or run:

       source "$HOME/.cargo/env"
```

```{warning}
   Do not install Rust or Cargo with your system package manager (for example `sudo apt install cargo`). Distribution packages are often outdated and too old to build cjseq. If you already installed them this way, remove them with `sudo apt remove cargo rustc` before continuing.
```

2. Open a new terminal (or Command Prompt on Windows) and check that Cargo is version 1.85 or newer:

```
   cargo --version
```

   If the version is older, run `rustup update stable`.

3. Install cjseq:

```
   cargo install cjseq
```

4. Verify the installation with:

```
   cjseq --help
```

If the cjseq's usage is displayed, the installation has been successful. 

(installing-uicityjson)=
## Installing the LoD 2.2 CityJSON Generator

The LoD 2.2 CityJSON Generator is distributed as a ready-to-use application for Windows and Linux. It does not require Python or any other package, only Roofer (see {ref}`installing-roofer`).

### Windows

1. Go to the [MultiRoofs CityJSON Generator releases page](https://github.com/MultiRoofs/UIcityJSON/releases) and download
   `MultiRoofs_CityJSON_Setup.exe` from the latest release.
2. Double-click `MultiRoofs_CityJSON_Setup.exe` and follow the steps of the installer.

3. Start **MultiRoofs** from the Start menu.

### Linux

These instructions have been tested on Ubuntu 24.04.5 LTS. You can install the application, or run it directly from an AppImage without installing it.

#### Option 1: Install the application

1. Go to the [MultiRoofs CityJSON Generator releases page](https://github.com/MultiRoofs/UIcityJSON/releases) and download
   `MultiRoofs-linux-x86_64.tar.gz` from the latest release.
2. Open a **Terminal** in the folder where you saved the file, then extract it and run the installer:

```
   tar -xzf MultiRoofs-linux-x86_64.tar.gz
   cd MultiRoofs-linux-x86_64
   ./install_multiroofs.sh
```

   By default, the application is installed for the current user only, and no root privileges are needed. To install it for all users of the computer, run instead:

```
   sudo ./install_multiroofs.sh --system
```

| | User installation (default) | System installation |
|---|---|---|
| Root needed | No | Yes |
| Application files | `~/.local/share/multiroofs` | `/opt/multiroofs` |
| Command | `~/.local/bin/multiroofs` | `/usr/local/bin/multiroofs` |
| Menu entry | `~/.local/share/applications` | `/usr/local/share/applications` |

3. Start **MultiRoofs** from the application menu, or run `multiroofs` in a terminal.

```{note}
If the `multiroofs` command is not found right after a user installation, log out and back in. Ubuntu adds `~/.local/bin` to the `PATH` at login once the folder exists. The menu entry works immediately.
```

To update the application, run the installer of the new version. To uninstall it, run:

```
   ./install_multiroofs.sh --uninstall
```

For a system installation, use `sudo ./install_multiroofs.sh --system --uninstall`.

#### Option 2: Run the AppImage

1. Go to the [MultiRoofs CityJSON Generator releases page](https://github.com/MultiRoofs/UIcityJSON/releases) and download
   `MultiRoofs-x86_64.AppImage` from the latest release.
2. Make it executable and start it:

```
   chmod +x MultiRoofs-x86_64.AppImage
   ./MultiRoofs-x86_64.AppImage
```

```{note}
Some AppImages need FUSE 2, which Ubuntu 24.04 does not install by default. If the AppImage fails with a FUSE error, either install it with `sudo apt install libfuse2t64`, or run the AppImage with `./MultiRoofs-x86_64.AppImage --appimage-extract-and-run`.
```

### Running from the source code

If you prefer not to install the application, you can run it from its source code with Python 3.11 or later. See the README of the [MultiRoofs CityJSON Generator repository](https://github.com/MultiRoofs/UIcityJSON/blob/main/README.md).