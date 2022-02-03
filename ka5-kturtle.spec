%define		kdeappsver	21.12.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kturtle
Summary:	kturtle
Summary(pl.UTF-8):	kturtle
Name:		ka5-%{kaname}
Version:	21.12.2
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ba730e06d8c02252f4ded6a753cc08c3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTurtle is an educational programming environment that aims to make
learning how to program as easily as possible. To achieve this KTurtle
makes all programming tools available from the user interface. The
programming language used is TurtleScript which allows its commands to
be translated.

%description -l pl.UTF-8
KTurtle to edukacyjne środowisko programistyczne, którego celem jest
nauczanie programowania tak łatwo, jak to tylko możliwe. Aby to osiągnąć
KTurtle udostępnia wszystkie narzędzia programistyczne z interfejsu
użytkownika. Używanym językiem programowania jest TurtleScript, który
pozwala by jego komendy były przetłumaczone.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kturtle.knsrc
%attr(755,root,root) %{_bindir}/kturtle
%{_desktopdir}/org.kde.kturtle.desktop
%{_iconsdir}/hicolor/128x128/apps/kturtle.png
%{_iconsdir}/hicolor/16x16/apps/kturtle.png
%{_iconsdir}/hicolor/22x22/apps/kturtle.png
%{_iconsdir}/hicolor/32x32/apps/kturtle.png
%{_iconsdir}/hicolor/48x48/apps/kturtle.png
%{_iconsdir}/hicolor/64x64/apps/kturtle.png
%dir %{_datadir}/katepart
%dir %{_datadir}/katepart/syntax
%{_datadir}/katepart/syntax/logohighlightstyle.en_GB.xml
%{_datadir}/katepart/syntax/logohighlightstyle.nb.xml
%{_datadir}/katepart/syntax/logohighlightstyle.nds.xml
%{_datadir}/katepart/syntax/logohighlightstyle.nl.xml
%{_datadir}/kturtle
%dir %{_datadir}/kxmlgui5/kturtle
%{_datadir}/kxmlgui5/kturtle/kturtleui.rc
%{_datadir}/metainfo/org.kde.kturtle.appdata.xml
