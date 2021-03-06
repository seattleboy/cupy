import cupy
from cupy.random import generator


# TODO(beam2d): Implement many distributions


def beta(a, b, size=None, dtype=float):
    """Beta distribution.

    Returns an array of samples drawn from the beta distribution. Its
    probability density function is defined as

    .. math::
       f(x) = \\frac{x^{\\alpha-1}(1-x)^{\\beta-1}}{B(\\alpha,\\beta)},

    Args:
        a (float): Parameter of the beta distribution :math:`\\alpha`.
        b (float): Parameter of the beta distribution :math:`\\beta`.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.float32` and
            :class:`numpy.float64` types are allowed.

    Returns:
        cupy.ndarray: Samples drawn from the beta distribution.

    .. seealso::
        :func:`cupy.random.RandomState.beta`
        :func:`numpy.random.beta`
    """
    rs = generator.get_random_state()
    return rs.beta(a, b, size, dtype)


def binomial(n, p, size=None, dtype=int):
    """Binomial distribution.

    Returns an array of samples drawn from the binomial distribution. Its
    probability mass function is defined as

    .. math::
        f(x) = \\binom{n}{x}p^x(1-p)^{n-x},

    Args:
        n (int): Trial number of the binomial distribution.
        p (float): Success probability of the binomial distribution.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.int32` and
            :class:`numpy.int64` types are allowed.

    Returns:
        cupy.ndarray: Samples drawn from the binomial distribution.

    .. seealso::
        :func:`cupy.random.RandomState.binomial`
        :func:`numpy.random.binomial`
    """
    rs = generator.get_random_state()
    return rs.binomial(n, p, size, dtype)


def gamma(shape, scale=1.0, size=None, dtype=float):
    """Gamma distribution.

    Returns an array of samples drawn from the gamma distribution. Its
    probability density function is defined as

    .. math::
       f(x) = \\frac{1}{\\Gamma(k)\\theta^k}x^{k-1}e^{-x/\\theta},

    Args:
        shape (array): Parameter of the gamma distribution :math:`k`.
        scale (array): Parameter of the gamma distribution :math:`\\theta`
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.float32` and
            :class:`numpy.float64` types are allowed.

    Returns:
        cupy.ndarray: Samples drawn from the gamma distribution.

    .. seealso::
        :func:`cupy.random.RandomState.gamma`
        :func:`numpy.random.gamma`
    """
    rs = generator.get_random_state()
    return rs.gamma(shape, scale, size, dtype)


def dirichlet(alpha, size=None, dtype=float):
    """Dirichlet distribution.

    Returns an array of samples drawn from the dirichlet distribution. Its
    probability density function is defined as

    .. math::
        f(x) = \\frac{\\Gamma(\\sum_{i=1}^K\\alpha_i)} \
            {\\prod_{i=1}^{K}\\Gamma(\\alpha_i)} \
            \\prod_{i=1}^Kx_i^{\\alpha_i-1},

    Args:
        alpha (array): Parameters of the dirichlet distribution
            :math:`\\alpha`.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.float32` and
            :class:`numpy.float64` types are allowed.

    Returns:
        cupy.ndarray: Samples drawn from the dirichlet distribution.

    .. seealso::
        :func:`cupy.random.RandomState.dirichlet`
        :func:`numpy.random.dirichlet`
    """
    rs = generator.get_random_state()
    return rs.dirichlet(alpha, size, dtype)


def gumbel(loc=0.0, scale=1.0, size=None, dtype=float):
    """Returns an array of samples drawn from a Gumbel distribution.

    The samples are drawn from a Gumbel distribution with location ``loc``
    and scale ``scale``.
    Its probability density function is defined as

    .. math::
       f(x) = \\frac{1}{\\eta} \
           \\exp\\left\\{ - \\frac{x - \\mu}{\\eta} \\right\\} \
           \\exp\\left[-\\exp\\left\\{-\\frac{x - \\mu}{\\eta} \
           \\right\\}\\right],

    where :math:`\\mu` is ``loc`` and :math:`\\eta` is ``scale``.

    Args:
        loc (float): The location of the mode :math:`\\mu`.
        scale (float): The scale parameter :math:`\\eta`.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.float32` and
            :class:`numpy.float64` types are allowed.

    Returns:
        cupy.ndarray: Samples drawn from the Gumbel distribution.

    .. seealso::
        :func:`cupy.random.RandomState.gumbel`
        :func:`numpy.random.gumbel`
    """
    rs = generator.get_random_state()
    return rs.gumbel(loc, scale, size, dtype)


def laplace(loc=0.0, scale=1.0, size=None, dtype=float):
    """Laplace distribution.

    Returns an array of samples drawn from the laplace distribution. Its
    probability density function is defined as

    .. math::
       f(x) = \\frac{1}{2b}\\exp\\left(-\\frac{|x-\\mu|}{b}\\right),

    Args:
        loc (float): The location of the mode :math:`\\mu`.
        scale (float): The scale parameter :math:`b`.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.float32` and
            :class:`numpy.float64` types are allowed.

    Returns:
        cupy.ndarray: Samples drawn from the laplace distribution.

    .. seealso::
        :func:`cupy.random.RandomState.laplace`
        :func:`numpy.random.laplace`
    """
    rs = generator.get_random_state()
    return rs.laplace(loc, scale, size, dtype)


def lognormal(mean=0.0, sigma=1.0, size=None, dtype=float):
    """Returns an array of samples drawn from a log normal distribution.

    The samples are natural log of samples drawn from a normal distribution
    with mean ``mean`` and deviation ``sigma``.

    Args:
        mean (float): Mean of the normal distribution.
        sigma (float): Standard deviation of the normal distribution.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.float32` and
            :class:`numpy.float64` types are allowed.

    Returns:
        cupy.ndarray: Samples drawn from the log normal distribution.

    .. seealso:: :func:`numpy.random.lognormal`

    """
    rs = generator.get_random_state()
    return rs.lognormal(mean, sigma, size=size, dtype=dtype)


def normal(loc=0.0, scale=1.0, size=None, dtype=float):
    """Returns an array of normally distributed samples.

    Args:
        loc (float or array_like of floats): Mean of the normal distribution.
        scale (float or array_like of floats):
            Standard deviation of the normal distribution.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier. Only :class:`numpy.float32` and
            :class:`numpy.float64` types are allowed.

    Returns:
        cupy.ndarray: Normally distributed samples.

    .. seealso:: :func:`numpy.random.normal`

    """
    rs = generator.get_random_state()
    x = rs.normal(0, 1, size, dtype)
    cupy.multiply(x, scale, out=x)
    cupy.add(x, loc, out=x)
    return x


def standard_normal(size=None, dtype=float):
    """Returns an array of samples drawn from the standard normal distribution.

    This is a variant of :func:`cupy.random.randn`.

    Args:
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier.

    Returns:
        cupy.ndarray: Samples drawn from the standard normal distribution.

    .. seealso:: :func:`numpy.random.standard_normal`

    """
    return normal(size=size, dtype=dtype)


def uniform(low=0.0, high=1.0, size=None, dtype=float):
    """Returns an array of uniformly-distributed samples over an interval.

    Samples are drawn from a uniform distribution over the half-open interval
    ``[low, high)``.

    Args:
        low (float): Lower end of the interval.
        high (float): Upper end of the interval.
        size (int or tuple of ints): The shape of the array. If ``None``, a
            zero-dimensional array is generated.
        dtype: Data type specifier.

    Returns:
        cupy.ndarray: Samples drawn from the uniform distribution.

    .. seealso:: :func:`numpy.random.uniform`

    """
    rs = generator.get_random_state()
    return rs.uniform(low, high, size=size, dtype=dtype)
