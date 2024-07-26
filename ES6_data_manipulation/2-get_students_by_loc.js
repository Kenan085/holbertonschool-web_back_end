function getListStudentsByLocation(students, city) {
  return students.filter((student) => student.location === city);
}
export default getListStudentsByLocation;
