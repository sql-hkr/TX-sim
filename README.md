# TX-sim
## 可飽和変流器
### 磁気ヒステリシスモデル
Jiles–Atherton モデルを採用する

> [!TIP]
> 詳しくは以下のURLを参照されたい
> 
> https://en.wikipedia.org/wiki/Jiles–Atherton_model

非履歴磁化

$$
M_{an}=(1-t)M_{an}^{iso}+tM_{an}^{aniso}
\xrightarrow{t=0}M_{an}^{iso}
$$

等方性

$$
M_{an}^{iso}=M_s\left[\coth\left(\frac{H+\alpha M}{a}\right)-\frac{a}{H+\alpha M}\right]
$$

$\delta\triangleq\text{sgn}\left(\frac{dH}{dt}\right)$

$$
\frac{dM}{dH}=\frac{1}{1+c}\frac{M_{an}-M}{\delta k-\alpha(M_{an}-M)}+\frac{c}{1+c}\frac{dM_{an}}{dH}
$$

$$
B(H)=\mu_0\left[H+M(H)\right]\approx \mu_0M(H) \quad \because |H|\ll |M|
$$

### 励磁回路
$$
\text{Faraday's law: }\oint_{\partial \Sigma}\mathbf{E}\cdot d\mathbf{\ell}=-\iint_\Sigma \frac{\partial \mathbf{B}}{\partial t}\cdot d\mathbf{S}
$$

$$
\mathcal{E}=-\frac{d\Phi}{dt}=-N_2\frac{d\phi}{dt}\approx -N_2\frac{d}{dt}(BS)
$$

$$
E_r=
\begin{cases}
    |\mathcal{E}|-v_d & \text{if }|\mathcal{E}|-v_d>0\\
    0 & \text{otherwise}
\end{cases}
\approx |\mathcal{E}| \quad \because v_d\ll |\mathcal{E}|
$$

$$
\sum_\text{loop}V_i=0\quad\to\quad E_r=R_fI_f+L_f\frac{dI_f}{dt}
$$

### 結果

![](fig/res.jpg)
