Name:           clr-optimized-link-scripts
Version:        2
Release:        2
Source0:        http://localhost/cgit/projects/clr-optimized-link-scripts/snapshot/clr-optimized-link-scripts-2.tar.xz
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
install -m 0644 -D clear_ordering_map.gold %{buildroot}/usr/share/clear/optimized-link-scripts/clear_ordering_map.gold
install -m 0644 -D clear_ordering_map.ld %{buildroot}/usr/share/clear/optimized-link-scripts/clear_ordering_map.ld
mkdir -p %{buildroot}/usr/share/clear/optimized-link-scripts/scripts.gold
mkdir -p %{buildroot}/usr/share/clear/optimized-link-scripts/scripts.ld
install -m 0644 scripts.gold/* %{buildroot}/usr/share/clear/optimized-link-scripts/scripts.gold
install -m 0644 scripts.ld/* %{buildroot}/usr/share/clear/optimized-link-scripts/scripts.ld

%files
/usr/share/clear/optimized-link-scripts/clear_ordering_map.gold
/usr/share/clear/optimized-link-scripts/clear_ordering_map.ld
/usr/share/clear/optimized-link-scripts/scripts.gold/*
/usr/share/clear/optimized-link-scripts/scripts.ld/*

