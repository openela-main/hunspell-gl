Name: hunspell-gl
Summary: Galician hunspell dictionaries
%global upstreamid 20080515
Version: 0.%{upstreamid}
Release: 16%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/800/2/corrector_ooo3.oxt
URL: http://wiki.mancomun.org/index.php/Corrector_ortogr%C3%A1fico_para_OpenOffice.org#Descrici.C3.B3n
License: GPLv2
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-gl)

%description
Galician hunspell dictionaries.

%prep
%autosetup -c -n hunspell-gl

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/*.dic dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc dictionaries/README-gl-ES.txt
%{_datadir}/myspell/*

%changelog
* Sat Jul 07 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.20080515-16
- Update Source tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080515-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080515-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080515-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.20080515-12
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20080515-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080515-1
- latest dictionaries

* Wed Apr 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080410-1
- latest dictionaries

* Fri Nov 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071107-1
- latest dictionaries

* Tue Aug 21 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070802-1
- latest dictionaries
- clarify license

* Sat May 05 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070504-1
- latest dictionaries

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20061002-1
- initial version
