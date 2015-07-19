# revision 31341
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-noindentafter
Version:	20131010
Release:	9
Summary:	TeXLive noindentafter package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noindentafter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noindentafter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive noindentafter package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/noindentafter/noindentafter.sty
%doc %{_texmfdistdir}/doc/latex/noindentafter/README
%doc %{_texmfdistdir}/doc/latex/noindentafter/dry.sty
%doc %{_texmfdistdir}/doc/latex/noindentafter/noindentafter.pdf
%doc %{_texmfdistdir}/doc/latex/noindentafter/noindentafter.tex
%doc %{_texmfdistdir}/doc/latex/noindentafter/packagedoc.cls
%doc %{_texmfdistdir}/doc/latex/noindentafter/with.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
