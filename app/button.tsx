'use client' 

import React from 'react';

const buttonClick = (e) => {
    console.log('click!');
}

function Button() {
    return(
        <button class='searchBtn' onClick={buttonClick}>Search!</button>
    );
}

export default Button;
