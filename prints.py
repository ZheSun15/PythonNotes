

def get_executable(build, rel_path):
    build_dir = build
    # use {} to pass variable by selecting their names.
    # similar to "some text {0}, {1}".format(VarName1, VarName2)
    returncodes.exit_with_driver_input_error(
                    "Could not find build '{build}' at {build_dir}. "
                    "Please run './build.py {build}'.".format(**locals()))