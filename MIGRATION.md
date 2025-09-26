# Migration Guide: Old Setup → New Virtual Environment Setup

If you previously used `installs_required.py` and are experiencing Jupyter kernel issues, here's how to migrate to the new virtual environment setup.

## 🚨 The Problem You're Experiencing

- **Error:** `No module named ipykernel_launcher`
- **Error:** `externally-managed-environment`
- **Issue:** VS Code can't find packages in Jupyter notebooks
- **Cause:** Homebrew Python 3.13+ restrictions and kernel registration issues

## 🔄 Migration Steps

### 1. Clean Slate (Recommended)
```bash
# Delete any existing problematic installations (optional)
pip uninstall jupyter jupyterlab ipykernel
# Or if using Homebrew:
brew uninstall jupyter jupyterlab
```

### 2. Run the New Setup
```bash
# In your python_setup_ds_101 folder:
python setup_python_environment.py
```

### 3. Clean Up Old Kernels (if needed)
```bash
# List existing Jupyter kernels:
jupyter kernelspec list

# Remove old problematic kernels:
jupyter kernelspec remove old_kernel_name
```

### 4. Restart VS Code
- **Completely close and reopen VS Code**
- **Select "Python (Digital Studies 101)" kernel in notebooks**

## 📋 What Changed

| Old Setup | New Setup |
|-----------|-----------|
| Global package installation | Virtual environment (`ds101_env/`) |
| System Python conflicts | Isolated environment |
| Manual kernel registration | Automatic kernel setup |
| Homebrew restrictions | Bypassed with venv |
| VS Code configuration issues | Auto-configured settings |

## ✅ Verification

Your migration worked if:
1. ✅ You can create a new `.ipynb` file in VS Code
2. ✅ "Python (Digital Studies 101)" appears as a kernel option  
3. ✅ This code runs without errors:
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   import plotly.express as px
   print("✅ Migration successful!")
   ```

## 🆘 If Migration Fails

1. **Try the complete reset:**
   ```bash
   # Remove everything and start fresh:
   rm -rf ds101_env
   jupyter kernelspec list  # Note any DS101 related kernels
   jupyter kernelspec remove ds101  # If it exists
   python setup_python_environment.py
   ```

2. **Check VS Code Python interpreter:**
   - `Ctrl+Shift+P` → "Python: Select Interpreter"
   - Choose the one in `ds101_env/bin/python` (or `ds101_env\Scripts\python.exe`)

3. **Manually register the kernel:**
   ```bash
   # Activate the environment first:
   source ds101_env/bin/activate  # macOS/Linux
   # OR
   ds101_env\Scripts\activate     # Windows
   
   # Then register:
   python -m ipykernel install --user --name ds101 --display-name "Python (Digital Studies 101)"
   ```

## 💡 Benefits of New Setup

- 🚫 **No more "externally-managed-environment" errors**
- 🚫 **No more missing ipykernel issues**  
- ✅ **Clean, isolated environment**
- ✅ **Easy to reset if problems occur**
- ✅ **Works with all Python versions/installations**
- ✅ **VS Code auto-configuration**

---

**Need help?** Create an issue with your error message and operating system: https://github.com/joostburgers/python_setup_ds_101/issues