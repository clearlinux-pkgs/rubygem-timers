Name     : rubygem-timers
Version  : 4.0.1
Release  : 5
URL      : https://rubygems.org/downloads/timers-4.0.1.gem
Source0  : https://rubygems.org/downloads/timers-4.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-docile
BuildRequires : rubygem-domain_name
BuildRequires : rubygem-hitimes
BuildRequires : rubygem-http-cookie
BuildRequires : rubygem-mime-types
BuildRequires : rubygem-netrc
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-term-ansicolor
BuildRequires : rubygem-thor
BuildRequires : rubygem-tins
BuildRequires : rubygem-unf
BuildRequires : rubygem-unf_ext
BuildRequires : rubygem-cucumber

%description
Timers
======
[![Gem Version](https://badge.fury.io/rb/timers.png)](http://rubygems.org/gems/timers)
[![Build Status](https://secure.travis-ci.org/celluloid/timers.png?branch=master)](http://travis-ci.org/celluloid/timers)
[![Code Climate](https://codeclimate.com/github/celluloid/timers.png)](https://codeclimate.com/github/celluloid/timers)
[![Coverage Status](https://coveralls.io/repos/celluloid/timers/badge.png?branch=master)](https://coveralls.io/r/celluloid/timers)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n timers-4.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-timers.gemspec

%build
gem build rubygem-timers.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
timers-4.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/timers-4.0.1
sed -i '/bundler/ s/^/#/' spec/spec_helper.rb
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
sed -i '/ruby-prof/ s/^/#/' spec/performance_spec.rb

rspec -I.:lib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/timers-4.0.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/%3e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/cancel%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/cancelled%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/cdesc-Handle.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/fire-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/Handle/to_f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/bisect_left-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/cdesc-Events.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/fire-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/first-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/pop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/schedule-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Events/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/after-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/cancel-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/cdesc-Group.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/continue-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/current_offset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/delay-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/events-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/every-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/fire-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/pause-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/paused_timers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/resume-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/timers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/wait-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Group/wait_interval-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/cancel-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/cdesc-Timer.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/continue-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/delay-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/fire-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/fires_in-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/interval-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/offset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/pause-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/paused%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/recurring-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Timer/resume-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Wait/cdesc-Wait.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Wait/duration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Wait/for-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Wait/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Wait/remaining-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Wait/time_remaining%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/Wait/while_time_remaining-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/Timers/cdesc-Timers.ri
/usr/lib64/ruby/gems/2.2.0/doc/timers-4.0.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/.coveralls.yml
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/AUTHORS.md
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/CHANGES.md
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/lib/timers.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/lib/timers/events.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/lib/timers/group.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/lib/timers/timer.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/lib/timers/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/lib/timers/wait.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/cancel_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/events_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/every_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/group_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/performance_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/strict_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/spec/timeout_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/timers-4.0.1/timers.gemspec
/usr/lib64/ruby/gems/2.2.0/specifications/timers-4.0.1.gemspec
