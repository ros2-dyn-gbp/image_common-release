%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-camera-calibration-parsers
Version:        3.1.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS camera_calibration_parsers package

License:        BSD
URL:            http://ros.org/wiki/camera_calibration_parsers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rcpputils
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-yaml-cpp-vendor
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-cmake-ros
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-sensor-msgs
BuildRequires:  ros-rolling-yaml-cpp-vendor
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
camera_calibration_parsers contains routines for reading and writing camera
calibration parameters.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Jan 14 2022 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.2-1
- Autogenerated by Bloom

* Fri Dec 17 2021 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.1-1
- Autogenerated by Bloom

* Tue Jun 29 2021 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.1.0-1
- Autogenerated by Bloom

* Wed May 26 2021 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 3.0.0-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Michael Carroll <michael@openrobotics.org> - 2.3.0-2
- Autogenerated by Bloom

