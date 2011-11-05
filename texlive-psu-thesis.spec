# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/psu-thesis
# catalog-date 2008-09-20 13:36:26 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-psu-thesis
Version:	1.1
Release:	1
Summary:	Package for writing a thesis at Penn State University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/psu-thesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psu-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psu-thesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides proper page formatting according to the
Penn State thesis office guidelines (as of 2004) and
automatically formats the front and back matter, title page,
and more. A BibTeX style file is also included for the
bibliography.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/psu-thesis/psuthesis.bst
%{_texmfdistdir}/tex/latex/psu-thesis/psu-thesis.sty
%doc %{_texmfdistdir}/doc/latex/psu-thesis/README
%doc %{_texmfdistdir}/doc/latex/psu-thesis/manual.pdf
%doc %{_texmfdistdir}/doc/latex/psu-thesis/manual.tex
%doc %{_texmfdistdir}/doc/latex/psu-thesis/mssample.pdf
%doc %{_texmfdistdir}/doc/latex/psu-thesis/mssample.tex
%doc %{_texmfdistdir}/doc/latex/psu-thesis/phdsample.pdf
%doc %{_texmfdistdir}/doc/latex/psu-thesis/phdsample.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
