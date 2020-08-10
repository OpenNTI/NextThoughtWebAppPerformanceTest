#!/bin/bash
TOKEN=$1
echo $TOKEN

COURSE_NTIIDS=( "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914049040_4744481198483187534"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895426_4744481198244697563"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895339_4744481197987404016"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914049011_4744481197536151624"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-381762027272797856_4744477175327467881"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895500_4744481198805620892"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635894588_4744481197214508490"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635894564_4744481197088118676"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895588_4744481199178767181"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914048981_4744481196940283859"
                "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914048953_4744481196655629595"
		"tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635897999_4744481499102048854" )

for i in "${COURSE_NTIIDS[@]}";
do
	http POST https://postgres-test01.nextthot.com/dataserver2/CourseAdmin/DropAllCourseEnrollments ntiid="$i" Authorization:"Bearer $TOKEN"
done
