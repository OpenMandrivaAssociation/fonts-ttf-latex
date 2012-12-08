
Summary:	LaTeX TrueType fonts for LyX
Name:		fonts-ttf-latex
Version:	0.1
Release:	%mkrel 13

# see README: these fonts were converted from the LaTeX .pfb forms,
#             and are under the respective licenses of the sources.
License:	Distributable

URL:		http://wiki.lyx.org/pmwiki.php/FAQ/Qt
Group:		System/Fonts/True type

Source0:	http://movementarian.org/latex-xft-fonts-%version.tar.gz

BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
Provides:	latex-xft-fonts

%description
This Package provides LaTeX TrueType fonts so that LyX can display LaTex
characters.

%prep
%setup -q -n latex-xft-fonts-%version

%build
perl -p -i -e "s|INSTALLDIR=.*|INSTALLDIR=%_datadir/fonts/TTF/latex|" Makefile

%install
rm -fr %buildroot
DESTDIR=%buildroot make install

(
cd %buildroot/%_datadir/fonts/TTF/latex/
# those are not unicode but in latex encoding
/usr/sbin/ttmkfdir -u | sed 's/iso10646-1/misc-fontspecific/' > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/latex \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-latex:pri=50

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc README
%dir %_datadir/fonts/TTF/latex/
%_datadir/fonts/TTF/latex/*.ttf
%config(noreplace) %_datadir/fonts/TTF/latex/fonts.dir
%config(noreplace) %_datadir/fonts/TTF/latex/fonts.scale
%_sysconfdir/X11/fontpath.d/ttf-latex:pri=50




%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.1-12mdv2011.0
+ Revision: 675420
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.1-11
+ Revision: 675184
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-10
+ Revision: 664333
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-9mdv2011.0
+ Revision: 605199
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.1-8mdv2010.1
+ Revision: 494150
- fc-cache is now called by an rpm filetrigger

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1-7mdv2009.0
+ Revision: 220952
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2008.1
+ Revision: 149808
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.1-5mdv2008.0
+ Revision: 48745
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:11:58 (52893)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:12:57 (52819)
- import fonts-ttf-latex-0.1-2mdk

* Tue Feb 07 2006 Frederic Crozat <fcrozat@mandriva.com> 0.1-2mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)

* Wed Sep 03 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-1mdk
- initial release

