#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v2
# autospec commit: e661f3a
#
Name     : clr-optimized-link-scripts
Version  : 4
Release  : 4
URL      : http://localhost/cgit/projects/clr-optimized-link-scripts/snapshot/clr-optimized-link-scripts-v4.tar.xz
Source0  : http://localhost/cgit/projects/clr-optimized-link-scripts/snapshot/clr-optimized-link-scripts-v4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clr-optimized-link-scripts-data = %{version}-%{release}
Requires: clr-optimized-link-scripts-license = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Holding place for optimized linker scripts
Script creation:
1) perf record -e cycles:u,branch-misses -j any,u -a (outside of container before benchmark)
2) run benchmark
3) perf-hfsort -p perf.data --save bench1 -r /tmp/pts (wherever the path is to the root of where benchmarks were run)
- repeat 1-3 for as many benchmarks as desired
- perf-hfsort ---reload bench1,bench2,...,benchn -o sort-dir (consolidate bench marks for script creation)
- finalize-order.py -i sort-dir -t <ld|gold> -o scripts.<ld|gold> -m clear_ordering_map.<ld|gold> -p /usr/share/clear/optimized-link-scripts/scripts.<ld|gold> (create scripts)

%package data
Summary: data components for the clr-optimized-link-scripts package.
Group: Data

%description data
data components for the clr-optimized-link-scripts package.


%package license
Summary: license components for the clr-optimized-link-scripts package.
Group: Default

%description license
license components for the clr-optimized-link-scripts package.


%prep
%setup -q -n clr-optimized-link-scripts-v4
cd %{_builddir}/clr-optimized-link-scripts-v4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1700061176
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1700061176
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-optimized-link-scripts
cp %{_builddir}/clr-optimized-link-scripts-v%{version}/LICENSE %{buildroot}/usr/share/package-licenses/clr-optimized-link-scripts/8532c6d849f68016e932ae7abee616ac9c5d5d4e || :
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/clear/optimized-link-scripts/clear_ordering_map.gold
/usr/share/clear/optimized-link-scripts/clear_ordering_map.ld
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--bash.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--clang-16.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--emacs-29.1.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--emacsclient.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--gpg-agent.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--grep.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--lscpu.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--perf.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--php.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--ps.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--sshd.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--sudo.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--tmux.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--bin--vulkaninfo.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--extensions--no-debug-non-zts-20220829--opcache.so.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--glibc-hwcaps--x86-64-v3--libc.so.6.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--glibc-hwcaps--x86-64-v3--libm.so.6.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--ld-2.38.so.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libLLVM-16.so.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libassuan.so.0.8.6.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libclang-cpp.so.16.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libcrypto.so.3.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libevent_core-2.1.so.7.0.1.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libexpat.so.1.8.10.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libgcc_s.so.1.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libgcrypt.so.20.4.2.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libgmp.so.10.4.1.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libgpg-error.so.0.34.0.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libgtest.so.1.12.1.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libncursesw.so.6.4.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libnpth.so.0.1.2.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libnuma.so.1.0.0.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libpcre2-8.so.0.11.2.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libproc2.so.0.0.2.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libsnappy.so.1.1.10.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libstdc++.so.6.0.32.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libsystemd.so.0.35.0.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libvulkan.so.1.3.269.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--libxml2.so.2.11.5.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--systemd--libsystemd-core-252.so.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--lib64--systemd--libsystemd-shared-252.so.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--usr--libexec--sudo--libsudo_util.so.0.0.0.gold
/usr/share/clear/optimized-link-scripts/scripts.gold/--var--lib--phoronix-test-suite--installed-tests--pts--leveldb-1.1.0--leveldb-1.23--build--db_bench.gold
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--bash.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--clang-16.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--emacs-29.1.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--emacsclient.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--gpg-agent.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--grep.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--lscpu.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--perf.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--php.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--ps.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--sshd.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--sudo.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--tmux.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--bin--vulkaninfo.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--extensions--no-debug-non-zts-20220829--opcache.so.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--glibc-hwcaps--x86-64-v3--libc.so.6.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--glibc-hwcaps--x86-64-v3--libm.so.6.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--ld-2.38.so.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libLLVM-16.so.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libassuan.so.0.8.6.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libclang-cpp.so.16.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libcrypto.so.3.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libevent_core-2.1.so.7.0.1.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libexpat.so.1.8.10.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libgcc_s.so.1.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libgcrypt.so.20.4.2.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libgmp.so.10.4.1.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libgpg-error.so.0.34.0.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libgtest.so.1.12.1.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libncursesw.so.6.4.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libnpth.so.0.1.2.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libnuma.so.1.0.0.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libpcre2-8.so.0.11.2.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libproc2.so.0.0.2.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libsnappy.so.1.1.10.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libstdc++.so.6.0.32.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libsystemd.so.0.35.0.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libvulkan.so.1.3.269.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--libxml2.so.2.11.5.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--systemd--libsystemd-core-252.so.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--lib64--systemd--libsystemd-shared-252.so.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--usr--libexec--sudo--libsudo_util.so.0.0.0.ld
/usr/share/clear/optimized-link-scripts/scripts.ld/--var--lib--phoronix-test-suite--installed-tests--pts--leveldb-1.1.0--leveldb-1.23--build--db_bench.ld

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-optimized-link-scripts/8532c6d849f68016e932ae7abee616ac9c5d5d4e
