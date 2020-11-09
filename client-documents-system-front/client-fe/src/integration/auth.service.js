import api from './api'

export const AuthenticationService = {

    login: function (username, password) {
        return new Promise((resolve, reject) => {
            var formData = new FormData();
            formData.append('username', username)
            formData.append('password', password)
            api
                .post("/auth/token", formData)
                .then((response) => {
                    resolve(response.data)
                })
                .catch((response) => {
                    reject(response.status)
                })
        });
    },
}