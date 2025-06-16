%define		pkg	typescript
Summary:	TypeScript - language for application scale JavaScript development
Summary(pl.UTF-8):	TypeScript - język do rozwijania aplikacji w JavaScripcie
Name:		nodejs-%{pkg}
Version:	5.8.3
Release:	1
License:	Apache v2.0
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/typescript/-/%{pkg}-%{version}.tgz
# Source0-md5:	823004e76ca78f972a429156c829e9d6
URL:		https://www.typescriptlang.org/
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TypeScript is a language for application-scale JavaScript. TypeScript
adds optional types to JavaScript that support tools for large-scale
JavaScript applications for any browser, for any host, on any OS.
TypeScript compiles to readable, standards-based JavaScript.

%description -l pl.UTF-8
TypeScript to język dla aplikacji w JavaScripcie. Dodaje do
JavaScriptu opcjonalne typy ze wsparciem narzędzi dla wielkoskalowych
aplikacji dla dowolnej przeglądarki, dowolnego hosta, dowolnego
systemu operacyjnego. TypeScript kompiluje się do czytelnego,
opartego na standardach JavaScriptu.

%prep
%setup -qc
%{__mv} package/* .

%{__sed} -i -e '1s,^#!.*node,#!/usr/bin/node,' bin/*
chmod a+rx bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}

cp -pr bin lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

ln -s %{nodejs_libdir}/%{pkg}/bin/tsc $RPM_BUILD_ROOT%{_bindir}
ln -s %{nodejs_libdir}/%{pkg}/bin/tsserver $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md SECURITY.md
# symlinks
%{_bindir}/tsc
%{_bindir}/tsserver
%dir %{nodejs_libdir}/%{pkg}
%dir %{nodejs_libdir}/%{pkg}/bin
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/bin/tsc
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/bin/tsserver
%{nodejs_libdir}/%{pkg}/lib
%{nodejs_libdir}/%{pkg}/package.json
