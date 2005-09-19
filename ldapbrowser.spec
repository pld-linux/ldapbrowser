Summary:	LDAP Browser/Editor
Summary(pl):	Przegl±darka/edytor LDAP
Name:		ldapbrowser
Version:	2.82
%define	_beta	2
%define	_rel	6
Release:	0.b%{_beta}.%{_rel}
Epoch:		0
License:	?
Group:		Applications
%define	_ver %(echo %{version} | tr -d .)
Source0:	http://www-unix.mcs.anl.gov/~gawor/ldapcommon/bin/Browser%{_ver}b%{_beta}.tar.gz
# NoSource0-md5:	810f8a3940644e5a750a4feec00494ff
NoSource:	0
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

%description -l pl
Mo¿liwo¶ci:
- przegl±danie, przeszukiwanie i modyfikowanie DIT
- obs³uga LDIF
- wzorce obiektów
- obs³uga warto¶ci binarnych
- obs³uga LDAP v3
- obs³uga SSL
- interfejs przeci±gnij-i-upu¶æ, kopiuj-wklej
- nazwane sesje
- przegl±danie i modyfikowanie atrybutów.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.TXT LICENSE.ICONS *.html
%attr(755,root,root) %{_bindir}/lbe
%attr(755,root,root) %{_bindir}/ldapbrowser
%{_datadir}
