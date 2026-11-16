(mrio-cli-install)=
# Install the CLI-based MRIO

This guide explains how to install the CLI-based MRIO on your computer. CLI-based MRIO is written in Rust and distributed as source code, so you first download the code, then install Rust, and finally build MRIO on your own computer. Once these steps are complete, follow the {ref}`CLI-based MRIO tutorial <mrio-cli-tutorial>` to use it.

The installation consists of five steps:

1. Download the MRIO project.
2. Install Rust and Cargo.
3. Verify the installation.
4. Open a terminal in the MRIO project folder.
5. Build MRIO.

```{note}
MRIO requires Rust version 1.81 or newer, and an internet connection during installation and the first build.
```

## Download the MRIO project

Open the [MRIO GitHub repository](https://github.com/MultiRoofs/mrio) in a web browser, click **Code**, and then **Download ZIP** ({numref}`fig-cli-mrio-github`).

```{figure} ./images/mrio_githup.png
:width: 700px
:align: center
:alt: MRIO GitHub repository page
:name: fig-cli-mrio-github

The MRIO GitHub repository, where the source code can be downloaded with **Code** and **Download ZIP**.
```

When the download is complete, extract the ZIP file to a convenient location, for example your **Downloads** folder:

```text
C:\Users\<username>\Downloads\mrio
```

```{admonition} Warning
:class: important
Do not work directly from inside the compressed ZIP file. Always extract it first.
```

The extracted folder contains the source code, example datasets, configuration files and other files needed to build and run MRIO. One of them is `Cargo.toml`, which identifies the folder as a Rust project. If you are familiar with Git, you can clone the repository instead with:

```bash
git clone https://github.com/MultiRoofs/mrio.git
```

## Install Rust

MRIO is built with Cargo, Rust's package manager and build system. The easiest way to install Rust and Cargo is with **rustup**, the official Rust installer.

### On Windows

1. Download the installer from the [rustup website](https://rustup.rs/) ({numref}`fig-cli-mrio-rust`).
2. Open the installer. A command-line window appears with these options:

   ```text
   1) Proceed with standard installation (default - just press enter)
   2) Customize installation
   3) Cancel installation
   ```

3. Press **Enter** to choose the standard installation.

```{figure} ./images/rust_download.png
:width: 700px
:align: center
:alt: rustup installation page
:name: fig-cli-mrio-rust

The rustup website, where the Rust installer can be downloaded.
```

The standard installation installs **Rust**, **Cargo** and **rustup**.

```{note}
If the installer reports that the Visual Studio C++ build tools are missing, follow its instructions to install them. Rust needs them to build programs on Windows.
```

### On macOS and Linux

Open a terminal and run:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Then choose the standard installation.

% TODO: confirm that MRIO builds on macOS and Linux, and add any platform-specific requirements.

## Verify the installation

After the installation is complete, close the installation window and **open a new terminal** (Command Prompt, PowerShell or Windows Terminal on Windows). A terminal that was already open before the installation may not recognise the new commands.

In the new terminal, check the Rust version:

```bash
rustc --version
```

Then check Cargo:

```bash
cargo --version
```

Both commands should return a version number, for example:

```text
rustc 1.xx.x
cargo 1.xx.x
```

The Rust version must be 1.81 or newer. If it is older, update it with:

```bash
rustup update
```

## Open a terminal in the MRIO project folder

Cargo commands must be run from inside the MRIO project folder. Move to it with the `cd` command, replacing the path with the location of your folder:

```bash
cd C:\Users\<username>\Downloads\mrio
```

On Windows, you can also open the MRIO folder in File Explorer, click the address bar, type `cmd` and press **Enter**. A Command Prompt opens directly in that folder ({numref}`fig-cli-mrio-cmd`).

```{figure} ./images/MRIO_CMD.png
:width: 700px
:align: center
:alt: Opening Command Prompt from the MRIO project folder
:name: fig-cli-mrio-cmd

Opening a Command Prompt directly from the MRIO folder through the File Explorer address bar.
```

To check that you are in the right folder, list its contents with `dir` (Windows) or `ls` (macOS and Linux). The list should include `Cargo.toml`.

## Build MRIO

In the terminal, run:

```bash
cargo build --release
```

During the first build, Cargo downloads and compiles the libraries MRIO depends on. This can take several minutes and it is normal that many messages appear in the terminal. When the command finishes without an error, MRIO is ready to use.

## Troubleshooting

| Problem | Solution |
|---|---|
| `rustc` or `cargo` is not recognised | Make sure the installation finished, then open a new terminal. |
| The Rust version is older than 1.81 | Run `rustup update`. |
| `could not find Cargo.toml` | The terminal is not in the MRIO folder. Move to it with `cd`. |
| The build fails with an error about a linker or build tools | On Windows, install the Visual Studio C++ build tools when the Rust installer asks for them. |

## Next steps

MRIO is now installed. Continue with {ref}`Starting MRIO <mrio-cli-start>` in the CLI-based MRIO tutorial.