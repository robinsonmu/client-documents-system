import { AuthenticationService } from '../integration/auth.service'
import jwtUtils from "../utils/jwt";
const TOKEN_KEY = 'token';

const state = {
    isAuthenticated: false,
    token: localStorage.getItem(TOKEN_KEY) || "",
    user: {}
};

const actions = {
    login(context, credentials) {
        return new Promise((resolve, reject) => {
            AuthenticationService.login(credentials.username, credentials.password)
                .then((data) => {
                    console.log(credentials);
                    console.log(data);
                    localStorage.setItem(TOKEN_KEY, data.access_token);
                    context.commit("authenticate", data.access_token)
                    resolve();
                })
                .catch((e) => {
                    console.log(e);
                    localStorage.removeItem(TOKEN_KEY)
                    reject();
                });
        });

    },

    createSessionFromToken({ dispatch, getters, commit }) {
        return new Promise((resolve, reject) => {
            let tokenSize = getters.getToken.length;
            if (tokenSize > 0) {
                if (!jwtUtils.tokenIsValid(getters.getToken)) {
                    // Token is expired
                    dispatch("revokeAuthToken").then(() => {
                        reject();
                    });
                } else {
                    // Token has not expired, and session may be needed to recreate
                    if (!getters.isAuthenticated) {
                        commit("authenticate", getters.getToken);
                    }
                    resolve();
                }
            } else {
                reject();
            }
        });
    },
    revokeAuthToken({ commit }) {
        return new Promise((resolve) => {
            localStorage.removeItem(TOKEN_KEY);
            commit("logout");
            resolve();
        });
    },
}

const mutations = {
    authenticate(state, token) {
        state.token = token;
        state.isAuthenticated = true;
        const tokenBody = jwtUtils.parseJwt(token);
        state.user = {
            email: tokenBody.sub
        }
    },
    logout(state) {
        state.token = "";
        state.isAuthenticated = false;
        state.user = {};
    },
}

const getters = {
    isAuthenticated: (state) => state.isAuthenticated,
    getToken: (state) => state.token,
    getUser: (state) => state.user,
};

export default { namespaced: true, state, actions, mutations, getters };

