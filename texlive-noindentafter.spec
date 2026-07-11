%global tl_name noindentafter
%global tl_revision 59195

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.00
Release:	%{tl_revision}.1
Summary:	Prevent paragraph indentation after environments or macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/noindentafter
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noindentafter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noindentafter.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noindentafter.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package, as the name suggests, supplies tools to automatically
suppress indentations in following paragraphs, specifically those
following a particular macro or environment.

