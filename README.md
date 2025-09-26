# Digital Studies 101 - Python Environment Setup

This guide explains how to set up a proper Python environment for the Digital Studies 101 course that works correctly with VS Code and Jupyter notebooks, avoiding the "externally-managed-environment" error.

## 🚀 Quick Start

**IMPORTANT:** This setup creates a virtual environment to avoid conflicts with your system Python (especially Homebrew Python on macOS).

## Prerequisites

1. **Visual Studio Code** installed on your system
2. **Python 3.8+** installed on your system (Homebrew Python 3.13 works great!)
3. **Git** installed on your system (for cloning the repository)
4. **Internet connection** for downloading packages and extensions

## Step 1: Get the Setup Files

### Option A: Using Git (Recommended)

1. **Open VS Code**
2. **Open the integrated terminal:**
   - Press `` Ctrl+` `` (backtick) OR
   - Go to `View` → `Terminal`

3. **Navigate to where you want to store the setup files:**
   ```bash
   cd Documents    # or wherever you prefer to keep your course files
   ```

4. **Clone the setup repository:**
   ```bash
   git clone https://github.com/joostburgers/python_setup_ds_101.git
   ```

5. **Navigate into the cloned folder:**
   ```bash
   cd python_setup_ds_101
   ```

6. **Open the folder in VS Code:**
   ```bash
   code .
   ```

### Option B: Download ZIP (Alternative)
1. Go to: https://github.com/joostburgers/python_setup_ds_101
2. Click "Code" → "Download ZIP"
3. Extract to your desired location
4. Open the folder in VS Code

## Step 2: Run the NEW Setup Script

**Important:** We now use a single improved script that creates a virtual environment and sets everything up properly.

### Using VS Code's Integrated Terminal

1. **Make sure you're in the `python_setup_ds_101` folder in VS Code**

2. **Open the integrated terminal:**
   - Press `` Ctrl+` `` (backtick) OR
   - Go to `View` → `Terminal`

3. **Run the new setup script:**
   ```bash
   python setup_python_environment.py
   ```
   
   *If `python` doesn't work, try:*
   ```bash
   python3 setup_python_environment.py
   ```

4. **Wait for completion** (this can take 15-30 minutes)
   - Watch for ✅ green checkmarks indicating success
   - The script will create a virtual environment called `ds101_env`
   - It will install all packages in the isolated environment
   - It will set up a Jupyter kernel for VS Code

## Step 3: Install VS Code Extensions (Optional but Recommended)

After the Python environment setup completes:

```bash
python install_vscode_extensions.py
```

## Step 4: Restart VS Code and Test

1. **Completely close and restart VS Code**
2. **Open the `python_setup_ds_101` folder again**
3. **Create a test notebook:**
   - Create a new file: `test.ipynb`
   - VS Code will prompt you to select a kernel
   - **Choose "Python (Digital Studies 101)"** from the kernel list
4. **Test the environment:**
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   import plotly.express as px
   print("✅ Environment is working!")
   ```

## 🔧 What This Setup Does (Technical Details)

The new setup script solves the Jupyter kernel problem by:

1. **Creating an isolated virtual environment** (`ds101_env/`)
2. **Installing all packages in the virtual environment** (no conflicts with system Python)
3. **Registering a Jupyter kernel** that VS Code can use
4. **Configuring VS Code settings** to use the correct Python interpreter
5. **Bypassing Homebrew's "externally-managed" restrictions**

## Troubleshooting

### ❌ "externally-managed-environment" Error
**This is fixed by the new setup!** The virtual environment bypasses this Homebrew restriction.

### ❌ "No module named ipykernel_launcher"
**This is fixed by the new setup!** The script installs `ipykernel` in the virtual environment.

### ❌ Python/Python3 Not Found
**Solutions:**
1. **Try `python3` instead of `python`:**
   ```bash
   python3 setup_python_environment.py
   ```

2. **Use full Python path (if Homebrew):**
   ```bash
   /opt/homebrew/bin/python3 setup_python_environment.py
   ```

3. **Fix Python PATH or reinstall with PATH option**

### ❌ VS Code Not Detecting the Kernel
**Solutions:**
1. **Restart VS Code completely** (close all windows)
2. **Reload the window:** `Ctrl+Shift+P` → "Developer: Reload Window"
3. **Manually select interpreter:** `Ctrl+Shift+P` → "Python: Select Interpreter" → Browse to `ds101_env/bin/python` (or `ds101_env\Scripts\python.exe` on Windows)

### ❌ Packages Not Found in Jupyter
**This means the wrong kernel is selected:**
1. **Click the kernel name** in the top-right of your notebook
2. **Select "Python (Digital Studies 101)"** from the list
3. **If not visible:** Restart VS Code and try again

## 🧠 Why Virtual Environments?

**The Problem:** 
- Homebrew Python 3.13+ is "externally managed" 
- Cannot install packages globally with pip
- System Python conflicts with course packages
- Jupyter kernels get confused about which Python to use

**The Solution:**
- Virtual environment isolates your course packages
- No conflicts with system/Homebrew Python
- Clean, reproducible environment
- Easy to reset if something breaks

## Advanced Usage

### Manually Activate the Environment
If you need to use the terminal directly:

**macOS/Linux:**
```bash
source ds101_env/bin/activate
```

**Windows:**
```bash
ds101_env\Scripts\activate
```

### Reset Everything
If something goes wrong, delete the `ds101_env` folder and re-run:
```bash
rm -rf ds101_env  # macOS/Linux
rmdir /s ds101_env  # Windows
python setup_python_environment.py
```

### Check What's Installed
```bash
# Activate environment first (see above)
pip list
```

## ✅ Verification Steps

### Test Your Environment
```bash
# This should work without errors:
python -c "import pandas, matplotlib, plotly, nltk, spacy; print('✅ All packages working!')"
```

### Test Jupyter in VS Code
1. **Create a new notebook:** `test.ipynb`
2. **Select the kernel:** "Python (Digital Studies 101)"
3. **Run this test cell:**
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   import plotly.express as px
   print("✅ Environment is working!")
   print(f"Pandas version: {pd.__version__}")
   ```

### Check VS Code Extensions
1. **Open Extensions panel:** `Ctrl+Shift+X`
2. **Look for:** Python, Jupyter, Rainbow CSV extensions

## 📝 Quick Summary for Students

**New simple process:**
1. Clone or download this repository
2. Open it in VS Code
3. Run: `python setup_python_environment.py`
4. Wait for completion (15-30 minutes)
5. Restart VS Code
6. Select "Python (Digital Studies 101)" kernel in notebooks

**What this fixes:**
- ✅ "externally-managed-environment" errors
- ✅ "No module named ipykernel_launcher" errors  
- ✅ Jupyter kernel registration issues
- ✅ Package conflicts between system/Homebrew Python

## 📚 After Setup: Using Your Environment

### Starting New Projects
1. **Copy the `ds101_env` folder** to your new project
2. **Or:** Create a new virtual environment using the same packages

### Working with Course Materials
1. **Always select the "Python (Digital Studies 101)" kernel**
2. **If packages are missing:** They're probably in a different kernel

### Sharing Your Work
- **Don't commit `ds101_env/`** to git (add to `.gitignore`)
- **Share your requirements:** Use `pip freeze > requirements.txt`

## 🆘 Getting Help

If you encounter issues:

1. **Read the error message carefully**
2. **Try the troubleshooting steps above**  
3. **Check the GitHub Issues:** https://github.com/joostburgers/python_setup_ds_101/issues
4. **Ask for help with:**
   - Your operating system
   - The exact error message
   - What step failed

---

**Setup Repository:** https://github.com/joostburgers/python_setup_ds_101

**Additional Resources:**
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Jupyter in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
