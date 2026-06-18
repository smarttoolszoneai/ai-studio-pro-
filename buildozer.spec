[app]

# (str) Title of your application
title = Panjtan CS

# (str) Package name
package.name = panjtancs

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# یہاں ہم نے moviepy اور اس کی ضروری لائبریریز شامل کی ہیں
requirements = python3,kivy==2.1.0,kivymd,moviepy,decorator,tqdm,requests

# (str) Custom source folders for requirements
# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is to use PythonActivity
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# صرف arm64-v8a رکھیں تاکہ بلڈ جلدی ہو اور نئے موبائلز پر چلے
android.archs = arm64-v8a

# (bool) enables Android auto backup
android.allow_backup = True

# (bool) Accept SDK license agreements
# یہ لائن سب سے اہم ہے گٹ ہب ایکشنز کے لیے
android.accept_sdk_license = True

# (str) The directory where the build is done
build_dir = ./.buildozer

# (str) The directory where bin/ is located
bin_dir = ./bin

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
