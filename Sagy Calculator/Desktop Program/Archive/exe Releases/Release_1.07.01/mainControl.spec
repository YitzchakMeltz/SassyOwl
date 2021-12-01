# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\hmeltz\\Documents\\GitHub\\DesktopCalculator\\mainControl.py'],
             pathex=['C:\\Users\\hmeltz\\Documents\\GitHub\\SassyOwl\\Sagy Calculator\\Desktop Program\\Archive\\exe Releases\\Release_1.07.01'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='mainControl',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\hmeltz\\Documents\\GitHub\\DesktopCalculator\\icons\\CalculatorLogo(150p)_1.0.0.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mainControl')
