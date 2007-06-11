Summary:	MP3 and Ogg tag editor
Summary(pl.UTF-8):	Edytor znaczników MP3 i Ogg
Name:		tagtool
Version:	0.12.3
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/tagtool/%{name}-%{version}.tar.bz2
# Source0-md5:	447b3a505fee68a82f25dcda9377b676
URL:		http://pwp.netcabo.pt/paol/tagtool/
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	id3lib-devel
BuildRequires:	libglade2 >= 2.4.0
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
  and/or organize them into directories. File names can be based on
  the contents of the tag.
- Create Playlists. Playlists can be sorted by file name or by any tag
  field.

The mass tag and mass rename features can handle filenames in any
format thanks to an easily configurable format template.

%description -l pl.UTF-8
Audio Tag Tool to program do zarządzania polami informacyjnymi
w plikach MP3 i Ogg Vorbis, najczęściej zwanymi znacznikami lub
"tagami".

Tag Tool może być użyty do edycji znaczników jeden po jednym, ale
najbardziej użyteczną cechą jest zdolność do łatwego pisania
znaczników czy zamiany setek plików na raz w każdym pożądanym
formacie.

Interfejs jest podzielony na dwie sekcje, z listą dostępnych plików
po lewej i zestawem etykiet po prawej. Każda etykieta odpowiada jako
jedna z głównych operacji jaką Audio Tag Tool potrafi zrobić:

- Edytor znaczników pozwala modyfikować znaczniki indywidualnie
- Oznaczanie wielu plików: można ustawić znaczniki w wielu plikach
  jednocześnie. Pola znaczników mogą być ustawione na ustaloną
  wartość, wstawione automatycznie z nazwy pliku albo pozostawione bez
  zmian.
- Czyszczenie znaczników pozwala na usuwanie znaczników z wielu plików
  na raz. Dla plików MP3 jest możliwość wyboru czy usuwać znaczniki
  ID3v1 czy ID3v2.
- Przenoszenie/zmiana nazwy wielu plików: można zmienić nazwę wielu
  plikom na raz i/lub podzielić je na katalogi. Nazwy plików mogą być
  bazowane na zawartości znaczników.
- Tworzenie playlist. Playlisty mogą być sortowane po nazwie albo
  dowolnym znaczniku.

Możliwość masowego oznaczania lub zamiana nazwy znaczników może
dotyczyć dowolnego formatu plików dzięki łatwemu formatowi szablonu.

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

mv $RPM_BUILD_ROOT/%{_datadir}/locale/{ua,uk}

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
%{_iconsdir}/*/*/*/*
