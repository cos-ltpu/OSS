Name:          git-restrict
Version:       3.0
Release:       1%{?dist}
Summary:       Simple utility for git repository permission management 
Group:         Testing
License:       AGPL-3.0
URL:           https://github.com/parazyd/git-restrict
Source:        %{name}-%{version}.tar.gz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp, /bin/chmod, gcc
Requires:      /bin/bash

%description
A minimal utility that allows repository permission management based on ssh keys when used with the command directive in ssh's authorized_keys file.

%prep
%setup -q

%build
gcc -g git-restrict.c -o git-restrict

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 git-restrict %{buildroot}%{_bindir}
cp -p git-restrict %{buildroot}%{_bindir}

%files
%{_bindir}/git-restrict

%changelog
* Thu Jun 04 2021 <Чигажова>
- Added %{_bindir}/git-restrict
