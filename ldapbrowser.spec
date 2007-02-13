%define	_beta	b2
%define	_rel	8
%define	_ver %(echo %{version} | tr -d .)
Summary:	LDAP Browser/Editor
Summary(pl.UTF-8):	Przeglądarka/edytor LDAP
Name:		ldapbrowser
Version:	2.82
Release:	0.%{_beta}.%{_rel}
Epoch:		0
License:	?
Group:		Applications
Source0:	http://www-unix.mcs.anl.gov/~gawor/ldapcommon/bin/Browser%{_ver}%{_beta}.tar.gz
# NoSource0-md5:	810f8a3940644e5a750a4feec00494ff
NoSource:	0
Source1:	%{name}.desktop
Patch0:		%{name}-PLD.patch
URL:		http://www-unix.mcs.anl.gov/~gawor/ldap/
Requires:	jre >= 1.2.2
Requires:	jre-X11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir /usr/share/%{name}

%description
Features:
- Browsing, searching and editing of the DIT
- LDIF support
- Object templates
- Binary value support
- LDAP v3 aware
- SSL support
- Drag and drop, copy-and-paste interface
- Named sessions
- Attribute viewers/editors.

%description -l pl.UTF-8
Możliwości:
- przeglądanie, przeszukiwanie i modyfikowanie DIT
- obsługa LDIF
- wzorce obiektów
- obsługa wartości binarnych
- obsługa LDAP v3
- obsługa SSL
- interfejs przeciągnij-i-upuść, kopiuj-wklej
- nazwane sesje
- przeglądanie i modyfikowanie atrybutów.

%prep
%setup -q -n %{name}
%patch0 -p1
rm -f *.lnk *.bat
rm -f *.sample lbe.old*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_bindir}}

cp -a */ $RPM_BUILD_ROOT%{_datadir}
cp -a *.config *.jar $RPM_BUILD_ROOT%{_datadir}
install lbe.sh $RPM_BUILD_ROOT%{_bindir}/lbe
ln -s lbe $RPM_BUILD_ROOT%{_bindir}/ldapbrowser
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/ldapbrowser.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.TXT LICENSE.ICONS *.html
%attr(755,root,root) %{_bindir}/lbe
%attr(755,root,root) %{_bindir}/ldapbrowser
%{_desktopdir}/ldapbrowser.desktop
%{_datadir}
