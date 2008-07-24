%define name	gournal
%define version	0.5.1
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	GNOME hardwriting notepad
Version: 	%{version}
Release: 	%{release}

Source:		http://www.adebenham.com/debian/%{name}_%{version}-1.tar.bz2
URL:		http://www.adebenham.com/gournal/
License:	GPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:  ImageMagick

%description
Gournal is a note-taking application written for usage on Tablet-PCs.  It's
designed for usage with a stylus, not a mouse or keyboard.  It does not have
handwriting recognition but can be used in co-ordination with xstroke to
accept text.  The pages are saved as gzipped SVG files (not totally standard
yet but working on it).

Gournal looks/works just like a physical notebook with multiple pages.
Gournal has the following tools:
    * Fine/Normal/Medium/Think Pens
    * Eraser
    * Highliter
    * Typed Text
    * Time-stamp
    * Zoom
    * Infinite undo/redo
    * Delete entire strokes
    * Networkable pages
    * <Insert Images>
    * <Load a file as the background> 

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir/
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name
cp *.glade pixmaps/*.png $RPM_BUILD_ROOT/%_datadir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=Office;
Icon=%{name}
Name=Gournal
Comment=Handwriting notepad
Categories=Office/Accessories
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/pencil.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/pencil.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/pencil.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

