# Installing dependencies

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

Open a terminal and run the install script:

```
curl -fsSL https://raw.githubusercontent.com/3DBAG/roofer/refs/heads/main/distribution/install.sh | sh
```

If the folder `~/.local/bin` is not yet on your `PATH`, add this line to your shell profile
(for example `~/.bashrc` or `~/.zshrc`) and open a new terminal:

```
export PATH="$HOME/.local/bin:$PATH"
```

Then check the installation:

```
roofer --version
```

For more details, see the [Roofer installation guide](https://innovation.3dbag.nl/roofer/getting_started.html).

## Installing cjseq

[cjseq](https://github.com/cityjson/cjseq) is an open-source tool for converting between
CityJSONSeq and CityJSON.

1. Install the Rust compiler by following the instructions at
   [rust-lang.org](https://www.rust-lang.org/learn/get-started).
   
   When you install Rustup you’ll also get the latest stable version of the Rust build tool and package manager, also known as `Cargo`.
2. Open a new Command Prompt and run:

```
   cargo install cjseq
```