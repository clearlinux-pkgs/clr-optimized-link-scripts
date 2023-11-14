Name:           clr-optimized-link-scripts
Version:        1
Release:        1
Source0:        http://localhost/cgit/projects/clr-optimized-link-scripts/snapshot/clr-optimized-link-scripts-1.tar.xz
License:        Apache-2.0
Summary:        Optimized scripts for linking
Url:            https://clearlinux.org/
Group:          base

%description
Optimized scripts for linking

%prep
%setup -q -n clr-optimized-link-scripts-%version

%build

%install
install -m 0644 -D clear_ordering_map %{buildroot}/usr/share/clear/optimized-link-scripts/clear_ordering_map
mkdir -p %{buildroot}/usr/share/clear/optimized-link-scripts/scripts
install -m 0644 scripts/* %{buildroot}/usr/share/clear/optimized-link-scripts/scripts

%files
/usr/share/clear/optimized-link-scripts/clear_ordering_map
/usr/share/clear/optimized-link-scripts/scripts/*
