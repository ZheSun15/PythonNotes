

def get_executable(build, rel_path):
    build_dir = build
    # use {} to pass variable by selecting their names.
    returncodes.exit_with_driver_input_error(
                    "Could not find build '{build}' at {build_dir}. "
                    "Please run './build.py {build}'.".format(**locals()))