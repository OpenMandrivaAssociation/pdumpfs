Name:           pdumpfs
Version:        1.3
Release:        %mkrel 4
Summary:        Daily backup system which preserves every daily snapshot 
Group:          File tools
License:        GPL
URL:            http://namazu.org/~satoru/pdumpfs/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  ruby-devel 
BuildArch:      noarch

%description
pdumpfs is a simple daily backup system similar to Plan9's dumpfs which 
preserves every daily snapshot. pdumpfs is written in Ruby. You can access 
the past snapshots at any time for retrieving a certain day's file. 

pdumpfs constructs the snapshot YYYY/MM/DD in the destination directory. All 
source files are copied to the snapshot directory for the first time. On and 
after the second time, pdumpfs copies only updated or newly created files and 
stores unchanged files as hard links to the files of the previous day's 
snapshot for saving a disk space.

%prep
%setup -q

%build
%make
# add a correct shebang at the beggining of the file
perl -pi -e '$. == 1 && print "#\!/usr/bin/ruby\n"' pdumpfs

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir/
chmod 0755 pdumpfs
cp pdumpfs  $RPM_BUILD_ROOT/%_bindir/

mkdir -p $RPM_BUILD_ROOT/%_mandir/
cp -R  man/man8 $RPM_BUILD_ROOT/%_mandir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc ChangeLog README
%_bindir/*
%_mandir/man8/*


