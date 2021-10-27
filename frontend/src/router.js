import LabelingSection from './components/labeling/LabelingSection';
import QuizSection from './components/quiz/QuizSection';
import PVPSection from './components/pvp/PVPSection';
import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
        { path: '/', match: 'exact', component: QuizSection}, 
        { path: '/labeling', component: LabelingSection },
        { path: '/quiz', component: QuizSection },
        { path: '/pvp', component: PVPSection }
    ]

export const router = new VueRouter({
    mode: 'history',
    routes
})