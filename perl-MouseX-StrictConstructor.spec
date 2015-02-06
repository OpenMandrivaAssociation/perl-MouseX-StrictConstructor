%define upstream_name       MouseX-StrictConstructor
%define upstream_version    0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
License:	Artistic
Group:		Development/Perl
Summary:	Make your object constructors blow up on unknown attributes
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Mouse)
BuildArch:	noarch

%description
Make your object constructors blow up on unknown attributes

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor destdir=%{buildroot}
make

%check
make test

%install
%makeinstall_std
find %{buildroot} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find %{buildroot} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%files
%doc README Changes
%{perl_vendorlib}/MouseX/StrictConstructor.pm
%{_mandir}/man3/*

%changelog
* Tue May 17 2011 Bruno Cornec <bcornec@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 675789
- Import first version of MouseX-StrictConstructor-0.02
- create perl-MouseX-StrictConstructor

