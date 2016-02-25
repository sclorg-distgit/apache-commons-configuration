%global pkg_name apache-commons-configuration
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}


%global base_name       configuration
%global short_name      commons-%{base_name}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.9
Release:        8.13%{?dist}
Summary:        Commons Configuration Package

License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix}apache-commons-parent >= 26-7
BuildRequires:  %{?scl_prefix}maven-antrun-plugin
BuildRequires:  %{?scl_prefix}maven-assembly-plugin
BuildRequires:  %{?scl_prefix}maven-compiler-plugin
BuildRequires:  %{?scl_prefix}maven-doxia-sitetools
BuildRequires:  %{?scl_prefix}maven-install-plugin
BuildRequires:  %{?scl_prefix}maven-jar-plugin
BuildRequires:  %{?scl_prefix}javacc-maven-plugin
BuildRequires:  %{?scl_prefix}maven-javadoc-plugin
BuildRequires:  %{?scl_prefix}maven-plugin-bundle
BuildRequires:  %{?scl_prefix}maven-resources-plugin
BuildRequires:  %{?scl_prefix}maven-surefire-plugin
BuildRequires:  %{?scl_prefix}maven-surefire-provider-junit

BuildRequires:  %{?scl_prefix_java_common}apache-commons-beanutils
BuildRequires:  %{?scl_prefix_java_common}apache-commons-codec
BuildRequires:  %{?scl_prefix_java_common}apache-commons-collections
BuildRequires:  %{?scl_prefix}apache-commons-digester
BuildRequires:  %{?scl_prefix}apache-commons-jexl
BuildRequires:  %{?scl_prefix}apache-commons-jxpath
BuildRequires:  %{?scl_prefix_java_common}apache-commons-lang
BuildRequires:  %{?scl_prefix_java_common}apache-commons-logging
BuildRequires:  %{?scl_prefix}apache-commons-vfs
BuildRequires:  %{?scl_prefix_java_common}tomcat-servlet-3.0-api
BuildRequires:  %{?scl_prefix_java_common}xml-commons-resolver




%description
Configuration is a project to provide a generic Configuration
interface and allow the source of the values to vary. It
provides easy typed access to single, as well as lists of
configuration values based on a 'key'.
Right now you can load properties from a simple properties
file, a properties file in a jar, an XML file, JNDI settings,
as well as use a mix of different sources using a
ConfigurationFactory and CompositeConfiguration.
Custom configuration objects are very easy to create now
by just subclassing AbstractConfiguration. This works
similar to how AbstractList works.

%package        javadoc
Summary:        API documentation for %{pkg_name}


%description    javadoc
%{summary}.


%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%{__sed} -i 's/\r//' LICENSE.txt NOTICE.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file   : %{short_name} %{pkg_name}
%mvn_alias  : org.apache.commons:%{short_name}
# We skip tests because we don't have test deps (dbunit in particular).
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 1.9-8.13
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.9-8.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.9-8.11
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.9-8.10
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.9-8.9
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.9-8.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-8.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-8.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-8.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-8.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-8.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.9-8
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-7
- Add BuildRequires on apache-commons-parent >= 26-7

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-5
- Remove unneeded BR: maven-idea-plugin

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.9-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Michal Srb <msrb@redhat.com> - 1.9-2
- Build with xmvn

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-1
- Update to upstream version 1.9
- Update to currennt packaging guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-1
- Update to upstream 1.8
- Install NOTICE.txt file

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 1.6-7
- Update to current guidelines.
- Move to servlet 3.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 15 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-5
- Change ant dep groupId to org.apache.ant to fix build
- Versionless jar & javadocs
- Use maven 3 to build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-3
- tomcat5 -> tomcat6 BRs/Rs
- jakarta -> apache BRs/Rs

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-2
- Add license to javadoc subpackage

* Thu May 27 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-1
- Rename package (jakarta-commons-configuration->apache-commons-configuration)
- Build with maven instead of ant, drop deprecated patches
- Rebase, cleanups, drop epoch

* Thu Aug 20 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.4-7
- Fix description.
- Remove requires(post/postun) for javadoc subpackage.
- Use sed instead of dos2unix.

* Thu Aug 20 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.4-6
- Remove gcj support.
- Initial build for Fedora.

* Mon May 18 2009 Fernando Nasser <fnasser@redhat.com> - 0:1.4-5
- Fix license
- Fix source URL

* Wed Mar 18 2009 Yong Yang <yyang@redhat.com> - 0:1.4-4
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Thu Feb 05 2009 Yong Yang <yyang@redhat.com> - 0:1.4-3
- Fix release tag

* Wed Jan 14 2009 Yong Yang <yyang@redhat.com> - 0:1.4-2jpp
- Import from dbhole's maven 2.0.8 packages, initial building

* Mon Aug 13 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.4-1jpp
- Upgrade to 1.4
- Add pom file

* Thu May 03 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.2-3jpp
- Patch one test

* Wed Mar 07 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.2-2jpp
- Add gcj_support option
- Optionally build without maven

* Mon Feb 20 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.2-1jpp
- Upgrade to 1.2

* Mon Feb 20 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.1-2jpp
- Rebuild for JPP-1.7 and maven-1.1

* Thu Sep 15 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.1-1jpp
- Upgrade to 1.1
- Omit findbugs and tasks reports: don't have these plugins yet
- Requires java 1.4.2 to build

* Mon Feb 21 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0.f-1jpp
- Upgrade to 1.0 final, letter in version can be bumped with 1.1
- Prepare for build with maven, but still build with ant

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0.d3-2jpp
- Rebuild with ant-1.6.2
- Upgrade to Ant 1.6.X
* Mon Jan 19 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.d3-1jpp
- First JPackage release
