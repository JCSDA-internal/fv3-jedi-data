# (C) Copyright 2017-2023 UCAR.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

################################################################################
# FV3-JEDI Test Files
################################################################################

cmake_minimum_required( VERSION 3.3.2 FATAL_ERROR )

project( fv3_jedi_data VERSION 1.5.0 DESCRIPTION "FV3-JEDI Test Files" )

find_package( ecbuild QUIET )
include( ecbuild_system NO_POLICY_SCOPE )
ecbuild_declare_project()
set( CMAKE_DIRECTORY_LABELS ${PROJECT_NAME} )

# Add tests to validate observation data files
find_package(ioda REQUIRED)

file( GLOB OBS_FILES testinput_tier_1/obs/*.nc4 testinput_tier_1/obs/*.nc )

foreach ( f ${OBS_FILES} )
        message($f)
        get_filename_component(filename ${f} NAME)

        # Note: IODA_YAML_ROOT is provided by find_package(ioda).
        # The ObsSpace.yaml file is *not* a test file. It always exists.
        ecbuild_add_test(
                TARGET ufo_data_validate_${filename}
                COMMAND ioda-validate.x
                LABELS ufo_data_validate
                ENVIRONMENT "ECKIT_COLOUR_OUTPUT=1"
                ARGS "--ignore-warn"
                     "--ignore-error"
                     "${IODA_YAML_ROOT}/validation/ObsSpace.yaml"
                     "${f}"
                )
endforeach()

ecbuild_print_summary()
