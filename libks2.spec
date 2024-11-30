Name:		libks2
Version:	2.0.6
Release:	1%{?dist}
Summary:	SignalWire's LibKitchenSink

Group:		Libraries/C and C++
License:	MIT
URL:		https://signalwire.com/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	cmake, libuuid-devel, openssl-devel, libatomic
Requires:	libuuid, openssl-libs, libatomic

%description
SignalWire LibKitchenSink

%package devel
Summary:	Develoment package for SignalWire's LibKitchenSink
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development package for SignalWire LibKitchenSink

%prep
%setup -q


%build
#configure
cmake . -DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags}


%install
%make_install


%files
/usr/lib64/libks2.so.*
%doc
/usr/share/doc/libks2/copyright

%files devel
/usr/include/*
/usr/lib64/lib*so
/usr/lib64/pkgconfig/libks2.pc


%changelog
* Sat Nov 30 2024 S-P Chan
- initial packaging
