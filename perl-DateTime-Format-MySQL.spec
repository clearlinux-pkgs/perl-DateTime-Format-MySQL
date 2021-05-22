#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-MySQL
Version  : 0.06
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/X/XM/XMIKEW/DateTime-Format-MySQL-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XM/XMIKEW/DateTime-Format-MySQL-0.06.tar.gz
Summary  : 'Parse and format MySQL dates and times'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-DateTime-Format-MySQL-license = %{version}-%{release}
Requires: perl-DateTime-Format-MySQL-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Format::Builder)

%description
This module handles formatting and parsing of MySQL date and time
related data types.

%package dev
Summary: dev components for the perl-DateTime-Format-MySQL package.
Group: Development
Provides: perl-DateTime-Format-MySQL-devel = %{version}-%{release}
Requires: perl-DateTime-Format-MySQL = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-MySQL package.


%package license
Summary: license components for the perl-DateTime-Format-MySQL package.
Group: Default

%description license
license components for the perl-DateTime-Format-MySQL package.


%package perl
Summary: perl components for the perl-DateTime-Format-MySQL package.
Group: Default
Requires: perl-DateTime-Format-MySQL = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-MySQL package.


%prep
%setup -q -n DateTime-Format-MySQL-0.06
cd %{_builddir}/DateTime-Format-MySQL-0.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-MySQL
cp %{_builddir}/DateTime-Format-MySQL-0.06/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-MySQL/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::MySQL.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-MySQL/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/DateTime/Format/MySQL.pm
