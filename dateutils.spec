Summary:	Command-line date and time calculation, conversion, and comparison
Name:		dateutils
Version:	0.4.6
Release:	1
License:	BSD
Group:		Applications/Console
Source0:	https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	d4fa0e85953e4d31491a67729d4b4af1
URL:		http://www.fresse.org/dateutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools which revolve around fiddling with dates and times on the
command line, with a strong focus on use cases that arise when dealing
with large amounts of financial data.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--without-old-links \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%preun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.tzmcc
%{_datadir}/%{name}/locale
