Summary:	MP3 and Ogg tag editor
Summary(pl):	Edytor znacznik�w MP3 i Ogg
Name:		tagtool
Version:	0.12
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/tagtool/%{name}-%{version}.tar.gz
# Source0-md5:	43a05e1b84ffb5639986788b1cf3c5b1
URL:		http://pwp.netcabo.pt/paol/tagtool/
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	id3lib-devel
BuildRequires:	libglade >= 2.4.0
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio Tag Tool is a program to manage the information fields in MP3
and Ogg Vorbis files, commonly called tags.

Tag Tool can be used to edit tags one by one, but the most useful
features are the ability to easily tag or rename hundreds of files at
once, in any desired format.

The interface is arranged into two sections, with the list of
available files on the left and a set of tabs on the right. Each tab
corresponds to one of the main operations Audio Tag Tool can do:

- Tag Editor lets you edit the tags individually.
- Tag Multiple Files: you can set the tags of multiple files at once.
  The tag fields can be set to a fixed value, filled in automatically
  from the file's name, or left alone.
- Clear Tags allows you to remove the tags from multiple files at
  once. For MP3 files it lets you choose to remove only ID3v1 or ID3v2
  tags.
- Move/Rename Multiple Files: you can rename multiple files at once
  and/or organize them into directories. File names can be based on the
  contents of the tag.
- Create Playlists. Playlists can be sorted by file name or by any tag
  field.

The mass tag and mass rename features can handle filenames in any
format thanks to an easily configurable format template.

%description -l pl
Audio Tag Tool to program do zarz�dzania polami informacyjnymi
w plikach MP3 i Ogg Vorbis, najcz�ciej zwanymi znacznikami lub
"tagami".

Tag Tool mo�e by� u�yty do edycji znacznik�w jeden po jednym, ale
najbardziej u�yteczn� cech� jest zdolno�� do �atwego pisania
znacznik�w czy zamiany setek plik�w na raz w ka�dym po��danym
formacie.

Interfejs jest podzielony na dwie sekcje, z list� dost�pnych plik�w
po lewej i zestawem etykiet po prawej. Ka�da etykieta odpowiada jako
jedna z g��wnych operacji jak� Audio Tag Tool potrafi zrobi�:

- Edytor znacznik�w pozwala modyfikowa� znaczniki indywidualnie
- Oznaczanie wielu plik�w: mo�na ustawi� znaczniki w wielu plikach
  jednocze�nie. Pola znacznik�w mog� by� ustawione na ustalon�
  warto��, wstawione automatycznie z nazwy pliku albo pozostawione bez
  zmian.
- Czyszczenie znacznik�w pozwala na usuwanie znacznik�w z wielu plik�w
  na raz. Dla plik�w MP3 jest mo�liwo�� wyboru czy usuwa� znaczniki
  ID3v1 czy ID3v2.
- Przenoszenie/zmiana nazwy wielu plik�w: mo�na zmieni� nazw� wielu
  plikom na raz i/lub podzieli� je na katalogi. Nazwy plik�w mog� by�
  bazowane na zawarto�ci znacznik�w.
- Tworzenie playlist. Playlisty mog� by� sortowane po nazwie albo
  dowolnym znaczniku.

Mo�liwo�� masowego oznaczania lub zamiana nazwy znacznik�w mo�e
dotyczy� dowolnego formatu plik�w dzi�ki �atwemu formatowi szablonu.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.dtd
%{_datadir}/%{name}/*.glade
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
