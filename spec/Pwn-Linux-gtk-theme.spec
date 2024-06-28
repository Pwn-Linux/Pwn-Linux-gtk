Name:           Pwn-Linux-gtk-theme
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Pwn Linux gtk themeing highly inspired by macOS
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/Pwn-Linux
Source0:        %{url}/Pwn-Linux-gtk/archive/master/Pwn-Linux-gtk-main.tar.gz

%description
Pwn Linux gtk themeing highly inspired by macOS

%prep
%setup -q -n Pwn-Linux-gtk-main

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes
cp -r Pwn %{buildroot}%{_datadir}/themes/

%files
%license LICENSE.md
%doc README.md
%{_datadir}/themes/Pwn

%changelog
{{{ git_dir_changelog }}}