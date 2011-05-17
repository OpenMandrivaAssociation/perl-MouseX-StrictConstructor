%define upstream_name       MouseX-StrictConstructor
%define upstream_version    0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    Artistic
Group:      Development/Perl
Summary:    Make your object constructors blow up on unknown attributes
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Make your object constructors blow up on unknown attributes

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/
make

%check
make test

%install
rm -rf %buildroot
make install DESTDIR=${RPM_BUILD_ROOT}
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/MouseX/StrictConstructor.pm
%{_mandir}/man3/*
