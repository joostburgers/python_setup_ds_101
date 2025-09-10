# Running Installation Scripts in Visual Studio Code

This guide explains how to run the Digital Studies 101 installation scripts directly from Visual Studio Code.

## Prerequisites

1. **Visual Studio Code** installed on your system
2. **Python 3.8+** installed on your system
3. **Python Extension** for VS Code (we'll install this if needed)

## Method 1: Using VS Code's Integrated Terminal (Recommended)

### Step 1: Open the Project in VS Code

1. **Open VS Code**
2. **Open the folder:**
   - Click `File` → `Open Folder...`
   - Navigate to your course folder: `ds_101_python_lessons`
   - Click `Select Folder`

### Step 2: Open the Integrated Terminal

1. **Open terminal in VS Code:**
   - Press `` Ctrl+` `` (backtick) OR
   - Go to `View` → `Terminal` OR
   - Press `Ctrl+Shift+P` and type "Terminal: Create New Terminal"

2. **Verify you're in the right directory:**
   - The terminal should show the path to your course folder
   - You should see files like `installs_required.py` and `install_vscode_extensions.py`

### Step 3: Run the Scripts

#### For Package Installation:
```bash
python installs_required.py
```

#### For VS Code Extensions Installation:
```bash
python install_vscode_extensions.py
```

### Step 4: Monitor Progress

- Watch the terminal output for installation progress
- Green checkmarks ✅ indicate successful installations
- Red X marks ❌ indicate failures that may need manual attention

## Method 2: Using VS Code's Python Extension Run Feature

### Step 1: Install Python Extension (if not already installed)

1. **Open Extensions panel:**
   - Press `Ctrl+Shift+X` OR
   - Click the Extensions icon in the left sidebar

2. **Search for "Python":**
   - Type "Python" in the search box
   - Install the official **Python** extension by Microsoft

### Step 2: Select Python Interpreter

1. **Open Command Palette:**
   - Press `Ctrl+Shift+P`

2. **Select interpreter:**
   - Type "Python: Select Interpreter"
   - Choose your Python installation (should show version 3.8+)

### Step 3: Run the Scripts

1. **Open the script file:**
   - Click on `installs_required.py` or `install_vscode_extensions.py` in the file explorer

2. **Run the script:**
   - Press `F5` OR
   - Right-click in the editor → "Run Python File in Terminal" OR
   - Click the ▶️ play button in the top-right corner OR
   - Press `Ctrl+F5` to run without debugging

## Method 3: Using VS Code Tasks (Advanced)

### Step 1: Create a Tasks Configuration

1. **Open Command Palette:** `Ctrl+Shift+P`
2. **Type:** "Tasks: Configure Task"
3. **Select:** "Create tasks.json from template"
4. **Choose:** "Others"

### Step 2: Configure Tasks

Replace the content of `.vscode/tasks.json` with:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Install Python Packages",
            "type": "shell",
            "command": "python",
            "args": ["installs_required.py"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "problemMatcher": []
        },
        {
            "label": "Install VS Code Extensions",
            "type": "shell", 
            "command": "python",
            "args": ["install_vscode_extensions.py"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "problemMatcher": []
        },
        {
            "label": "Install Everything",
            "dependsOrder": "sequence",
            "dependsOn": [
                "Install Python Packages",
                "Install VS Code Extensions"
            ],
            "group": "build"
        }
    ]
}
```

### Step 3: Run Tasks

1. **Open Command Palette:** `Ctrl+Shift+P`
2. **Type:** "Tasks: Run Task"
3. **Choose:**
   - "Install Python Packages" - for package installation
   - "Install VS Code Extensions" - for extension installation  
   - "Install Everything" - for both (runs sequentially)

## Troubleshooting

### Python Not Found
**Error:** `'python' is not recognized as an internal or external command`

**Solutions:**
1. **Try `python3` instead of `python`:**
   ```bash
   python3 installs_required.py
   ```

2. **Use full Python path:**
   ```bash
   C:\Users\[YourUsername]\AppData\Local\Programs\Python\Python313\python.exe installs_required.py
   ```

3. **Fix Python PATH:**
   - Reinstall Python with "Add to PATH" option checked
   - Or manually add Python to your system PATH

### VS Code Extensions Script Fails
**Error:** VS Code command not found

**Solutions:**
1. **Reinstall VS Code** with "Add to PATH" option
2. **Restart VS Code** after installation
3. **Run as Administrator** if on Windows

### Permission Errors
**Error:** Permission denied or access errors

**Solutions:**
1. **Run VS Code as Administrator** (Windows)
2. **Check file permissions** in terminal:
   ```bash
   ls -la *.py  # On macOS/Linux
   dir *.py     # On Windows
   ```

### Network/Download Issues
**Error:** Timeout or connection errors

**Solutions:**
1. **Check internet connection**
2. **Try running scripts one at a time**
3. **Use a VPN** if behind restrictive firewall
4. **Run during off-peak hours** for large downloads

## Post-Installation

### Verify Python Packages
```bash
python -c "import pandas, matplotlib, plotly, nltk, spacy; print('All packages imported successfully!')"
```

### Verify VS Code Extensions
1. **Open Extensions panel:** `Ctrl+Shift+X`
2. **Check installed extensions:** Look for Python, Jupyter, etc.

### Test Jupyter Notebooks
1. **Open a `.ipynb` file** in VS Code
2. **Select Python kernel** when prompted
3. **Run a test cell** to verify everything works

## Tips for Students

1. **Always use the integrated terminal** - keeps everything in one place
2. **Read the output carefully** - it shows exactly what's happening
3. **Don't panic if something fails** - most issues can be fixed by re-running
4. **Ask for help early** - don't struggle alone with installation issues
5. **Keep VS Code updated** - newer versions have better Python support

## Next Steps

After successful installation:

1. **Restart VS Code** to activate all extensions
2. **Open a Jupyter notebook** to test the environment
3. **Configure Git** if you haven't already:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
4. **Start working** on your Digital Studies assignments!

---

**Need Help?** 
- Check the VS Code Python tutorial: https://code.visualstudio.com/docs/python/python-tutorial
- Python extension documentation: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Course discussion forum or office hours
