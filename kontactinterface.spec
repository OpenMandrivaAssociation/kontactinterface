
Summary:        Kontact Plugin Interface Library
Name:           kontactinterface
Version:	23.08.5
Release:	1
License:        GPLv2+
Group:          System/Base
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Gui)

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5IconThemes)

BuildRequires:  boost-devel

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%description
Kontact Plugin Interface Library

%files -f kontactinterfaces5.lang
%{_datadir}/qlogging-categories5/kontactinterface.categories
%{_datadir}/qlogging-categories5/kontactinterface.renamecategories

#--------------------------------------------------------------------

%define kf5kontactinterface_major 5
%define oldlibkf5kontactinterface %mklibname kf5kontactinterface 5
%define libkf5kontactinterface %mklibname kpimkontactinterface

%package -n %libkf5kontactinterface
Summary:      Kontact Plugin Interface Library
Group:        System/Libraries
Requires:     %name = %version-%release
Obsoletes:    %mklibname kf5kontactinterface 4
Obsoletes:    %{mklibname kf5kontactinterface 5}

%description -n %libkf5kontactinterface
Kontact Plugin Interface Library

%files -n %libkf5kontactinterface
%_libdir/libKPim5KontactInterface.so.%{kf5kontactinterface_major}*

#--------------------------------------------------------------------

%define oldkf5kontactinterface_devel %mklibname kf5kontactinterface -d
%define kf5kontactinterface_devel %mklibname kpim5kontactinterface -d

%package -n %kf5kontactinterface_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %libkf5kontactinterface = %version-%release
Provides:       %name-devel = %{version}-%{release}
%rename %oldkf5kontactinterface_devel

%description -n %kf5kontactinterface_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kf5kontactinterface_devel
%_includedir/KPim5/KontactInterface
%_libdir/libKPim5KontactInterface.so
%_libdir/cmake/KPim5KontactInterface
%_libdir/qt5/mkspecs/modules/qt_KontactInterface.pri
%doc %{_docdir}/qt5/*.{tags,qch}

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang kontactinterfaces5
