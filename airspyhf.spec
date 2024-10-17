%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:           airspyhf
Version:        1.6.8
Release:        1%{?dist}
Summary:        Support programs for Airspy HF+ SDR
License:        BSD-3-Clause
URL:            https://www.airspy.com/airspy-hf-plus
#Git-Clone:     https://github.com/airspy/airspyhf.git
Source:         https://github.com/airspy/%{name}/archive/%{version}/%{name}-%{version}.tar.gz         
BuildRequires:  cmake
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(udev)

%description
Host software for Airspy HF+, a software defined radio
for the HF and VHF bands.

%package -n	%{libname}
Summary:        Driver for Airspy HF+

%description -n	%{libname}
Library to run Airspy HF+ SDR receiver.

%package -n	%{devname}
Summary:        Development files for Airspy HF+
Requires:       %{libname} = %{EVRD}

%description -n	%{devname}
Library headers for Airspy HF+ driver.

%package doc
Summary:        Documentation for Airspy HF+

%description doc
Documentation for Airspy HF+ driver.

%prep
%autosetup

%build
export CFLAGS="%{optflags} -lm"
%cmake -DINSTALL_UDEV_RULES=ON
%make_build

%install
%make_install -C build
rm %{buildroot}%{_libdir}/libairspyhf.a

mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspyhf.rules %{buildroot}%{_udevrulesdir}

%files
%{_udevrulesdir}/52-airspyhf.rules
%{_bindir}/airspyhf_calibrate
%{_bindir}/airspyhf_gpio
%{_bindir}/airspyhf_info
%{_bindir}/airspyhf_lib_version
%{_bindir}/airspyhf_rx

%files -n %{libname}
%{_libdir}/libairspyhf.so.*

%files -n %{devname}
%license LICENSE
%{_libdir}/libairspyhf.so
%{_includedir}/libairspyhf
%{_libdir}/pkgconfig/libairspyhf.pc

%files doc
%doc README.md
