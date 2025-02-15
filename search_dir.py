import os

def find_leaf_directories(directory):
    # Define directories to exclude from traversal.
    exclude_dirs = ['cmake-build-debug', '.git', '.idea']
    
    for root, dirs, _ in os.walk(directory):
        # Remove any excluded directories from the current list so that they are not traversed.
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Check if the current directory has no subdirectories (i.e., it's a leaf) and it's not the base directory.
        if not dirs and root != directory:
            relative_path = os.path.relpath(root, directory)
            print(f"include_directories({relative_path})")

# Replace with your actual directory path.
find_leaf_directories('/Users/sanghaoyu/CLionProjects/SIDM_mod_g4')

