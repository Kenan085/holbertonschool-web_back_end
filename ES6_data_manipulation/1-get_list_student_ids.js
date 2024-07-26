function getListStudentIds(students) {
    // Check if the input is an array
    if (!Array.isArray(students)) {
        return [];
    }

    // Use map to create an array of ids
    return students.map(student => student.id);
}

export default getListStudentIds;
