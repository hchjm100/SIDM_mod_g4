import os

def find_c_and_h_files(directory):
    for root, dirs, files in os.walk(directory):
        # Remove the 'cmake-build-debug' directory so os.walk doesn't traverse it.
        if 'cmake-build-debug' in dirs:
            dirs.remove('cmake-build-debug')
        for file in files:
            if file.endswith('.h') or file.endswith('.cc'):
                full_path = os.path.join(root, file)
                # Get the relative path by excluding the common base directory.
                relative_path = os.path.relpath(full_path, directory)
                print(relative_path)

# Replace with your actual directory
find_c_and_h_files('/Users/sanghaoyu/CLionProjects/SIDM_mod_g4')
